import streamlit as st 

# Select multiple Options

my_lang= ["Pathon", "julia", "Go", "Rust"]

choice = st.selectbox("Language" , my_lang)
st.write("You selected {}".format(choice))

# multiple Selection 

spoken_lang = ("English" , "French" , "Spanish" , "Twi")
my_spoken_lang = st.multiselect("Spoken Lang" , spoken_lang, default="English")

# Slider 
age = st.slider ("Age",1,100)

# Any Datatype
# Select Slider
color = st.select_slider("Choose color",options=["yellow","red","blue","black","white"]),value=("yellow","red") 
# value=("yellow","red") = eta diye default value dewa thakbe.
