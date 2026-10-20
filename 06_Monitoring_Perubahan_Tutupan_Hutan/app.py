import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Perubahan Tutupan Hutan", layout="wide")
st.title("Demonstrasi Perubahan Tutupan Hutan")
st.caption("Angka contoh dalam persen; bukan hasil penginderaan jauh atau pengukuran nyata.")
df=pd.read_csv("forest_change.csv")
df["perubahan_poin_persen"]=df["periode_2"]-df["periode_1"]
st.dataframe(df, use_container_width=True)
fig,ax=plt.subplots()
x=range(len(df))
ax.bar([i-0.18 for i in x],df["periode_1"],width=.36,label="Periode 1")
ax.bar([i+0.18 for i in x],df["periode_2"],width=.36,label="Periode 2")
ax.set_xticks(list(x),df["wilayah"]); ax.set_ylabel("Tutupan hutan (%)"); ax.legend()
st.pyplot(fig)
st.subheader("Perubahan")
for _,r in df.iterrows():
    arah="menurun" if r.perubahan_poin_persen<0 else "meningkat" if r.perubahan_poin_persen>0 else "tetap"
    st.write(f"- {r.wilayah}: {arah} {abs(r.perubahan_poin_persen)} poin persentase.")
st.warning("Untuk menyimpulkan deforestasi, diperlukan citra satelit yang sesuai, metode klasifikasi tervalidasi, pemeriksaan awan/resolusi, dan evaluasi kesalahan.")
