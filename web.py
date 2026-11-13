import streamlit as st

st.title("Meri Pehli Website")

w = st.slider("Button ki Width", 100, 500, 200)
h = st.slider("Button ki Height", 50, 300, 100)
color = st.color_picker("Button ka Color", "#FF0000")
text = st.text_input("Button pe kya likhna hai?", "Click Me")

st.markdown(f"""
<style>
button {{
width: {w}px !important;
height: {h}px !important;
background-color: {color} !important;
color: white !important;
font-size: 20px !important;
border-radius: 10px !important;
}}
</style>
""", unsafe_allow_html=True)

if st.button(text):
    st.balloons()
    st.success("Button dab gaya!")
