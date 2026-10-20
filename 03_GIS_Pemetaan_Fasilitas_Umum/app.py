import streamlit as st
import pandas as pd

st.set_page_config(page_title="Peta Fasilitas Umum", layout="wide")
st.title("Pemetaan Fasilitas Umum")
st.caption("Koordinat bersifat simulasi untuk demonstrasi GIS.")
df = pd.read_csv("facilities.csv")
jenis = st.multiselect("Filter jenis fasilitas", sorted(df["jenis"].unique()), default=sorted(df["jenis"].unique()))
view = df[df["jenis"].isin(jenis)]
st.metric("Fasilitas yang ditampilkan", len(view))
st.map(view.rename(columns={"latitude":"lat","longitude":"lon"})[["lat","lon"]], zoom=11)
st.dataframe(view, use_container_width=True)
st.write("**Interpretasi:** peta menampilkan sebaran titik berdasarkan koordinat. Analisis jarak atau cakupan layanan memerlukan data lokasi yang tervalidasi dan metode spasial tambahan.")
