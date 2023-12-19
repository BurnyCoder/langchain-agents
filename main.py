import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

user_animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow"))

if user_animal_type == "Cat":
    user_pet_color = st.sidebar.text_area("What color is your cat?", max_chars=15)

if user_animal_type == "Dog":
    user_pet_color = st.sidebar.text_area("What color is your dog?", max_chars=15)

if user_animal_type == "Cow":
    user_pet_color = st.sidebar.text_area("What color is your cow?", max_chars=15)

if user_pet_color:
    responce = lch.generate_pet_name(user_animal_type, user_pet_color)
    st.text(responce['pet_name']) 
