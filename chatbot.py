import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage

def run_chatbot():
    st.header("🤖 Chatbot Edukasi MBTI")
    st.caption("Diskusikan hasil MBTI kamu bersama AI")

    google_api_key = st.text_input("Google API Key", type="password")

    if not google_api_key:
        st.warning("Masukkan API Key dulu untuk mulai.")
        return

    if "agent" not in st.session_state:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=google_api_key,
            temperature=0.7 
        )
        st.session_state.agent = create_react_agent(
            model=llm,
            tools=[],
            prompt=f"Kamu adalah asisten edukasi MBTI. "
                   f"User memiliki hasil MBTI: {st.session_state.mbti_result}. "
                   "Berikan penjelasan, kekuatan, kelemahan, dan tips pengembangan."
        )
        st.session_state.messages = []

    # Tampilkan chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input chat
    prompt = st.chat_input("Tulis pertanyaan...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            messages = []
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    messages.append(AIMessage(content=msg["content"]))

            response = st.session_state.agent.invoke({"messages": messages})
            answer = response["messages"][-1].content if "messages" in response else "Maaf, ada error."

        except Exception as e:
            answer = f"Terjadi error: {e}"

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})
