import streamlit as st
import pandas as pd

# Judul Aplikasi
st.set_page_config(page_title="Rekomendasi Motor Mahasiswa", page_icon="🏍️")
st.title("🏍️ Sistem Rekomendasi Motor Budget Mahasiswa")
st.write("Temukan motor yang cocok buat ke kampus berdasarkan budgetmu!")

# Database sederhana motor (Bisa kamu kembangkan pakai CSV nanti)
data_motor = [
    {"nama": "Honda BeAT (2008-2010)", "harga": 3500000, "tipe": "Matic", "keunggulan": "Murah banget, sparepart melimpah", "irit": "Cukup"},
    {"nama": "Yamaha Mio J (2012)", "harga": 4000000, "tipe": "Matic", "keunggulan": "Sudah Injeksi, lincah buat selap-selip", "irit": "Irit"},
    {"nama": "Suzuki Nex II", "harga": 7500000, "tipe": "Matic", "keunggulan": "Mesin 'badak', jarang rewel, anti-mainstream", "irit": "Irit"},
    {"nama": "Honda Verza 150 (2014)", "harga": 7000000, "tipe": "Kopling", "keunggulan": "Gagah, irit banget untuk kelas 150cc", "irit": "Sangat Irit"},
    {"nama": "Honda Vario 125 (2019)", "harga": 15000000, "tipe": "Matic", "keunggulan": "Bagasi luas (muat helm), fitur modern", "irit": "Irit"},
    {"nama": "Yamaha Fazzio Hybrid", "harga": 16000000, "tipe": "Matic", "keunggulan": "Gaya Retro, teknologi Hybrid, cocok buat konten", "irit": "Sangat Irit"},
    {"nama": "Honda Supra X 125", "harga": 6000000, "tipe": "Bebek", "keunggulan": "Rajanya motor irit, perawatan paling murah", "irit": "Juara Irit"},
]

df = pd.DataFrame(data_motor)

# Sidebar untuk Filter
st.sidebar.header("Filter Pencarian")
budget_max = st.sidebar.slider("Pilih Budget Maksimal (Rp)", 3000000, 20000000, 10000000, step=500000)
tipe_motor = st.sidebar.multiselect("Pilih Tipe Motor", options=["Matic", "Kopling", "Bebek"], default=["Matic", "Kopling", "Bebek"])

# Logika Rekomendasi
hasil = df[(df['harga'] <= budget_max) & (df['tipe'].isin(tipe_motor))]

# Tampilan Hasil
st.subheader(f"Rekomendasi untuk Budget Rp{budget_max:,}")

if not hasil.empty:
    for index, row in hasil.iterrows():
        with st.expander(f"{row['nama']} - Rp{row['harga']:,}"):
            st.write(f"**Tipe:** {row['tipe']}")
            st.write(f"**Keunggulan:** {row['keunggulan']}")
            st.write(f"**Tingkat Keiritan:** {row['irit']}")
            st.button(f"Cek Detail {row['nama']}", key=index)
else:
    st.warning("Maaf bro, budget segitu belum dapet motor di list kita. Coba naikin dikit!")

# Tips
st.info("💡 **Tips:** Kalau beli motor bekas, jangan lupa bawa temen yang ngerti mesin atau cek ke bengkel terdekat ya!")