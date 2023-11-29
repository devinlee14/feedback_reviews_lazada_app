"""
Milestone 2
Nama: Devin Yaung Lee
Batch: HCK-009
program ini untuk mendeploy model
"""

import streamlit as st
import eda
import model

page = st.sidebar.selectbox(label="Select Page:", options=["Home Page", "Exploratory Data Analysis", "Predict Sentiment"])

if page == "Home Page":
    st.title("Home Page")
    st.write('')
    st.write("Milestone 2")
    st.write("Name  : Devin Yaung Lee")
    st.write("Batch : HCK-009")
    st.write("Aplikasi ini memiliki tujuan utama untuk menampilkan prediksi sentiment terhadap aplikasi lazada.")
    st.write('')
    st.write('')
    st.write('')

    with st.expander("Background Information"):
        st.caption("Dataset ini membahas tentang Reviews pada Aplikasi Lazada dari Google Store. Dimana pada data ini berisikan komentar-komentar atau feedback user ketika mereka menggunakan aplikasi tersebut. Feedback user ini ada yang memberikan feedback negatif, netral, maupun positif. Tujuan dari feedback ini adalah untuk mengetahui bagaimana pengalaman user dalam menggunakan aplikasi ini. Dengan mengetahui feedback ini, kita dapat mengetahui apa saja yang perlu dikembangkan untuk aplikasi lazada ini dan disesuaikan dengan keingininan user.Tujuan dilakukan modelin ini adalah untuk mengetahui sentiment dengan memasukan kalimat baru. Dimana dengan memasukan kalimat baru ini akan langsung terprediksi apakah feedback ini bersifat feedback negatif, netral, ataupun positif. Kegunaan dari predict ini kita dapat mengumpulkan data feedback untuk mengetahui apakah user menyukai aplikasi ini atau tidak.")
    with st.expander("Conclusion"):
        st.caption("""
        Dari analisa ini didapatkan beberapa hal, diantaranya :
        >1. Dataset ini memiliki jumlah rows 775,323 dan 8 columns
        >2. Berdasarkan dari visualisasi, rata-rata feedback user memiliki jumlah sepanjang 8000 huruf, yang menandakan user sangat terdorong untuk memberikan feedback secara detail
        >3. Model yang digunakan untuk dilakukan prediksi adalah Model LSTM
        >4. Hasil model masih mengindikasikan overfit, model ini masih dapat dikembangkan lebih lanjut dengan melakukan hyperparameter tuning, menambahkan layer, dan sebagainya.
        """)

elif page == "Exploratory Data Analysis":
    eda.run() # Calls the run function from eda

else:
    model.run() # Calls the run function from model