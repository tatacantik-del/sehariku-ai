import streamlit as st

st.set_page_config(page_title="SehariKu AI", page_icon="🤖", layout="centered")

# ======================
# FUNGSI AI SEDERHANA
# ======================
def hitung_skor(deadline, kesulitan, mood):
    skor = 0

    # skor dari deadline
    if deadline <= 1:
        skor += 3
    elif deadline <= 3:
        skor += 2
    else:
        skor += 1

    # skor dari kesulitan
    if kesulitan == "Sulit":
        skor += 2
    elif kesulitan == "Sedang":
        skor += 1

    # pengaruh mood
    if "Capek" in mood and kesulitan == "Sulit":
        skor -= 1
    if "Banyak tugas" in mood:
        skor += 1

    return skor


# ======================
# TAMPILAN
# ======================
st.title("🤖 SehariKu AI")
st.subheader("AI yang membantu mengatur kegiatan harian kamu")

nama = st.text_input("Masukkan nama kamu")

mood = st.selectbox(
    "Mood kamu hari ini",
    ["😊 Semangat", "😴 Capek", "😑 Biasa saja", "😵 Banyak tugas"]
)

st.markdown("---")
st.header("📚 Masukkan 3 Tugas Kamu")

# Tugas 1
st.subheader("Tugas 1")
tugas1 = st.text_input("Nama tugas 1")
deadline1 = st.number_input("Deadline tugas 1 (hari lagi)", min_value=0, max_value=30, key="d1")
kesulitan1 = st.selectbox("Kesulitan tugas 1", ["Mudah", "Sedang", "Sulit"], key="k1")

# Tugas 2
st.subheader("Tugas 2")
tugas2 = st.text_input("Nama tugas 2")
deadline2 = st.number_input("Deadline tugas 2 (hari lagi)", min_value=0, max_value=30, key="d2")
kesulitan2 = st.selectbox("Kesulitan tugas 2", ["Mudah", "Sedang", "Sulit"], key="k2")

# Tugas 3
st.subheader("Tugas 3")
tugas3 = st.text_input("Nama tugas 3")
deadline3 = st.number_input("Deadline tugas 3 (hari lagi)", min_value=0, max_value=30, key="d3")
kesulitan3 = st.selectbox("Kesulitan tugas 3", ["Mudah", "Sedang", "Sulit"], key="k3")

st.markdown("---")

if st.button("✨ Analisis Prioritas Tugas"):
    daftar_tugas = []

    if tugas1.strip() != "":
        daftar_tugas.append({
            "nama": tugas1,
            "deadline": deadline1,
            "kesulitan": kesulitan1,
            "skor": hitung_skor(deadline1, kesulitan1, mood)
        })

    if tugas2.strip() != "":
        daftar_tugas.append({
            "nama": tugas2,
            "deadline": deadline2,
            "kesulitan": kesulitan2,
            "skor": hitung_skor(deadline2, kesulitan2, mood)
        })

    if tugas3.strip() != "":
        daftar_tugas.append({
            "nama": tugas3,
            "deadline": deadline3,
            "kesulitan": kesulitan3,
            "skor": hitung_skor(deadline3, kesulitan3, mood)
        })

    if len(daftar_tugas) == 0:
        st.error("Isi minimal 1 tugas dulu yaa.")
    else:
        hasil = sorted(daftar_tugas, key=lambda x: x["skor"], reverse=True)

        st.header(f"📊 Hasil Analisis untuk {nama if nama else 'User'}")

        st.success(f"Tugas yang paling diprioritaskan: **{hasil[0]['nama']}**")

        st.subheader("Urutan Prioritas Tugas")
        for i, tugas in enumerate(hasil, start=1):
            st.write(
                f"{i}. **{tugas['nama']}** | Deadline: {tugas['deadline']} hari lagi | "
                f"Kesulitan: {tugas['kesulitan']} | Skor: {tugas['skor']}"
            )

        st.markdown("---")
        st.subheader("🤖 Saran AI")

        if "Capek" in mood:
            st.info("Kamu lagi capek, coba mulai dari tugas yang penting tapi kerjakan pelan-pelan ya.")
        elif "Semangat" in mood:
            st.info("Kamu lagi semangat, ini waktu yang bagus buat kerjakan tugas paling sulit dulu.")
        elif "Banyak tugas" in mood:
            st.info("Karena tugasmu banyak, fokus kerjakan yang deadline-nya paling dekat dulu.")
        else:
            st.info("Kerjakan tugas sesuai urutan prioritas supaya harimu lebih teratur.")