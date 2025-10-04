import streamlit as st

def run_quiz():
    st.header("📝 Kuis MBTI")
    st.write("Jawab pertanyaan berikut untuk mendeteksi tipe MBTI kamu:")

    # Extrovert vs Introvert
    q1 = st.radio("Kalau ada acara, kamu lebih suka?", ["Banyak orang", "Sedikit orang"])
    q2 = st.radio("Saat recharge energi, kamu lebih nyaman?", ["Ngobrol dengan orang lain", "Menyendiri"])
    q3 = st.radio("Kamu lebih sering dikenal sebagai?", ["Supel & ekspresif", "Tenang & pendiam"])

    # Sensing vs Intuition
    q4 = st.radio("Saat belajar hal baru, kamu lebih suka?", ["Fakta nyata & detail", "Ide & konsep besar"])
    q5 = st.radio("Kalau ada instruksi, kamu lebih suka?", ["Langkah-langkah jelas", "Tujuan umum & improvisasi"])
    q6 = st.radio("Kamu lebih percaya pada?", ["Pengalaman nyata", "Insting & imajinasi"])

    # Thinking vs Feeling
    q7 = st.radio("Saat membuat keputusan, kamu lebih condong ke?", ["Logika & objektif", "Nilai & perasaan"])
    q8 = st.radio("Kalau ada konflik, kamu biasanya?", ["Cari solusi rasional", "Pertimbangkan perasaan orang"])
    q9 = st.radio("Kamu lebih dikenal sebagai orang yang?", ["Tegas & analitis", "Peduli & harmonis"])

    # Judging vs Perceiving
    q10 = st.radio("Kamu lebih suka gaya hidup yang?", ["Teratur & terencana", "Fleksibel & spontan"])
    q11 = st.radio("Kalau kerja tugas, kamu biasanya?", ["Selesaikan jauh hari", "Deadline hunter 😅"])
    q12 = st.radio("Kalau liburan, kamu lebih suka?", ["Jadwal jelas", "Ikuti alur saja"])

    if st.button("🔍 Lihat Hasil MBTI"):
        # Hitung skor
        scores = {"E":0, "I":0, "S":0, "N":0, "T":0, "F":0, "J":0, "P":0}

        # Mapping jawaban ke skor
        if q1 == "Banyak orang (rame)": scores["E"]+=1
        else: scores["I"]+=1

        if q2 == "Ngobrol dengan orang lain": scores["E"]+=1
        else: scores["I"]+=1

        if q3 == "Supel & ekspresif": scores["E"]+=1
        else: scores["I"]+=1

        if q4 == "Fakta nyata & detail": scores["S"]+=1
        else: scores["N"]+=1

        if q5 == "Langkah-langkah jelas": scores["S"]+=1
        else: scores["N"]+=1

        if q6 == "Pengalaman nyata": scores["S"]+=1
        else: scores["N"]+=1

        if q7 == "Logika & objektif": scores["T"]+=1
        else: scores["F"]+=1

        if q8 == "Cari solusi rasional": scores["T"]+=1
        else: scores["F"]+=1

        if q9 == "Tegas & analitis": scores["T"]+=1
        else: scores["F"]+=1

        if q10 == "Teratur & terencana": scores["J"]+=1
        else: scores["P"]+=1

        if q11 == "Selesaikan jauh hari": scores["J"]+=1
        else: scores["P"]+=1

        if q12 == "Jadwal jelas": scores["J"]+=1
        else: scores["P"]+=1

        # Tentukan hasil
        tipe = ""
        tipe += "E" if scores["E"] >= scores["I"] else "I"
        tipe += "S" if scores["S"] >= scores["N"] else "N"
        tipe += "T" if scores["T"] >= scores["F"] else "F"
        tipe += "J" if scores["J"] >= scores["P"] else "P"

        st.session_state.mbti_result = tipe
        st.success(f"Tipe MBTI kamu adalah: **{tipe}**")
        st.session_state.quiz_done = True

        # Tombol lanjut ke chatbot
        if st.button("💬 Konsultasi MBTI"):
            st.session_state.page = "chatbot"
            st.rerun()
