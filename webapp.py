import numpy as np
import streamlit as st 
import streamlit.components.v1 as components
import pickle

import warnings
warnings.filterwarnings('ignore')

kmeans_model = pickle.load(open('kmeans.pkl', 'rb'))

def main():
    st.markdown("<h1 style='text-align: center; color: teal;'>Pemetaan Tingat Ancaman Tanah Longsor di Sinjai</h1>", unsafe_allow_html=True)

    html_file = open("map.html", 'r', encoding='utf-8')
    source_code = html_file.read()
    components.html(source_code, height=600)

    html_temp = """
    <div style="background-color:teal; padding:10px">
    <h2 style="color:white; text-align:center">Kmeans Clustering</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    city = ['Bulupoddo', 'Sinjai Barat', 'Sinjai Borong', 'Sinjai Selatan', 'Sinjai Tengah', 'Sinjai Timur', 'Sinjai Utara', 'Tellulimpoe']
    option = st.sidebar.selectbox("Which city would you like to predict?", city)
    st.subheader(option)
    st.spinner("Hello")
    kelurusan = st.text_input("Kelurusan", "Type Here")
    elevasi = st.text_input("Elevasi", "Type Here")
    geologi = st.text_input("Geologi", "Type Here")
    jalan = st.text_input("Jalan", "Type Here")
    kel = st.text_input("Kel", "Type Here")
    lahan = st.text_input("Lahan", "Type Here")
    sungai = st.text_input("Sungai", "Type Here")
    tanah = st.text_input("Tanah", "Type Here")
    hujan = st.text_input("Hujan", "Type Here")
    aspek = st.text_input("Aspek", "Type Here")

    

    if st.button("Predict"):
        input = np.array([[kelurusan, elevasi, geologi, jalan, kel, lahan, sungai, tanah, hujan, aspek]]).astype(np.float64)
        st.success(kmeans_model.predict(input))
    
if __name__ == "__main__":
    main()
