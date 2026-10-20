import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analisis Produktivitas Mahasiswa", layout="wide")
st.title("Analisis Faktor Produktivitas Belajar Mahasiswa")
st.caption("Demonstrasi edukasi menggunakan data sintetis, bukan data mahasiswa nyata.")

@st.cache_data
def make_data():
    rng = np.random.default_rng(17)
    n = 240
    tidur = rng.normal(7, 1.1, n).clip(3.5, 10)
    belajar = rng.normal(2.5, 1.0, n).clip(0.2, 6)
    hadir = rng.uniform(55, 100, n)
    skor = (35 + tidur*3 + belajar*4 + hadir*0.18 + rng.normal(0, 7, n)).clip(0, 100)
    return pd.DataFrame({"Jam tidur per malam": tidur.round(1),
                         "Jam belajar per hari": belajar.round(1),
                         "Kehadiran (%)": hadir.round(1),
                         "Indeks produktivitas (simulasi)": skor.round(1)})
df = make_data()
st.info("Angka dibuat secara acak untuk latihan analisis. Jangan gunakan untuk mengambil keputusan nyata.")
c1,c2,c3 = st.columns(3)
c1.metric("Jumlah data", len(df))
c2.metric("Rata-rata jam belajar", f"{df['Jam belajar per hari'].mean():.1f} jam")
c3.metric("Rata-rata indeks simulasi", f"{df['Indeks produktivitas (simulasi)'].mean():.1f}")
st.subheader("Data dan filter")
jam_min, jam_max = st.slider("Rentang jam belajar per hari", 0.0, 6.0, (0.0, 6.0), 0.1)
view = df[df["Jam belajar per hari"].between(jam_min, jam_max)]
st.dataframe(view, use_container_width=True)
st.subheader("Hubungan antarvariabel")
x = st.selectbox("Pilih faktor", ["Jam tidur per malam", "Jam belajar per hari", "Kehadiran (%)"])
fig, ax = plt.subplots()
ax.scatter(view[x], view["Indeks produktivitas (simulasi)"], alpha=.65)
ax.set_xlabel(x); ax.set_ylabel("Indeks produktivitas (simulasi)")
ax.set_title("Faktor dan indeks produktivitas simulasi")
st.pyplot(fig)
corr = view[[x, "Indeks produktivitas (simulasi)"]].corr().iloc[0,1] if len(view)>1 else np.nan
st.write(f"Korelasi pada data yang ditampilkan: **{corr:.2f}**" if pd.notna(corr) else "Data tidak cukup untuk menghitung korelasi.")
st.subheader("Kesimpulan awal")
st.write("Gunakan grafik dan korelasi sebagai petunjuk awal, bukan bukti sebab-akibat. Pada proyek nyata, gunakan data yang sah, dokumentasikan sumbernya, dan periksa kualitas data.")
