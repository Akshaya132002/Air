import streamlit as st
from PIL import Image
st.title("Ambient Air Quality Prediction using Machine Learning Algorithm")
#st.subheader("Air Quality Calculation System")
img = Image.open("airpol.jpg")
st.image(img)
option = st.selectbox(
    'Choose Your District',
    ('Madurai', 'Coimbatore', 'Chennai','Tirupur','Salem','Erode','Trichy','Nellai','Pollach'))

st.write('You selected:', option)
SO2 = st.number_input("Enter SO2 Level")
NO2 = st.number_input("Enter NO2 Level")
PM10 = st.number_input("Enter PM10 Level")
aqi = PM10
submit = st.button('Air Quality Index')
if aqi > 401:
    st.success("Severe")
    img1 = Image.open("severe.jpg")
    st.image(img1)
elif aqi > 301 and aqi <= 401:
    st.success("Very Poor")
    img4 = Image.open("very poor.jpg")
    st.image(img4)
elif aqi > 201 and aqi <=300:
    st.success("Poor")
    img3 = Image.open("satis.jpeg")
    st.image(img3)
elif aqi >101 and aqi <=200:
    st.success("Moderate")
    img5 = Image.open("mod.jpg")
    st.image(img5)
elif aqi > 51 and aqi<=100:
    st.success("Satisfactory")
    img6 = Image.open("satis.jpeg")
else:
    st.success("Good")
    img2 = Image.open("good.jpg")
    st.image(img2)





