"""
Milestone 2
Nama: Devin Yaung Lee
Batch: HCK-009
// eda.py //
program ini untuk mendeploy model EDA interface.
"""

import streamlit as st
import pandas as pd

# Function to run in app.py
def run():
    st.title("Explatoratory Data Analysis")

    df = pd.read_csv("LAZADA_REVIEWS.csv")

    # The first 5 data
    st.header("The first 5 data entry")
    st.table(df.head(5))

    # The last 5 data
    st.header("The last 5 data entry")
    st.table(df.tail(5))

    # Heatmap correlation
    st.header("Word Cloud")
    st.image("wordcloud.png", caption="Figure 1")
    with st.expander("Explanation"):
        st.caption(" Wordcloud memiliki kegunaan untuk melihat representasi text secara visual. Kata-kata dalam word cloud biasanya merupakan kata tunggal, dan pentingnya setiap kata ditunjukkan melalui ukuran font atau warna. Format ini berguna untuk cepat memahami istilah-istilah yang paling sering muncul untuk menentukan kepentingan dari kalimat tersebut. Dalam word cloud, ukuran setiap kata menunjukkan frekuensi atau kepentingannya: semakin besar dan tebal kata tersebut muncul, semakin sering kata itu disebutkan dalam teks yang diberikan, semakin menonjol pula kata tersebut. Dalam proses ini, akan dilihat kata apa saja yang paling sering muncul. Hal ini berguna untuk melihat seberapa related kata tersebut. Jika kata yang sering muncul tersebut ternyata tidak diperlukan, maka dapat dimasukan ke dalam stopwords agar terhindar dari bias")

    # Histogram Distribution of Customer Rating
    st.header("Reviews Length Distribution")
    st.image("reviewlenght.png", caption="Figure 2")
    with st.expander("Explanation"):
        st.caption("untuk mengetahui seberapa panjang teks yang ditulis pengguna dalam ulasan mereka. Hal ini bisa memberikan wawasan mengenai tingkat keterlibatan dan usaha yang pengguna berikan ketika memberikan ulasan. Ulasan yang panjang bisa menandakan bahwa pengguna tersebut sangat terdorong untuk berbagi pengalaman mereka secara detail, baik itu karena pengalaman yang sangat positif atau sangat negatif. Berdasarkan dari hasil visualisasi histogram, didapatkan bahwa kebanyakan user menulis lebih dari 8000 kata, yang menandakan bahwa user/pengguna tersebut sangat terdorong untuk memberikan feedback secara detail.")

    # Distribution of Cost of the Product
    st.header("Like Distribution")
    st.image("reviewrating.png", caption="Figure 3")
    with st.expander("Explanation"):
        st.caption("untuk memahami seberapa sering ulasan mendapat tanggapan positif dari pengguna lain. Dengan menganalisis distribusi ini, kita dapat mengetahui apakah ada ulasan tertentu yang menonjol karena banyaknya 'likes' yang diterima, yang dapat mengindikasikan bahwa ulasan tersebut sangat resonan dengan pengalaman atau pendapat pengguna lain.")