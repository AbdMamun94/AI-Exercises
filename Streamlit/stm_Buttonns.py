import streamlit as st

# working with Buttons

name = "Shuvo"

if st.button("Submit") :
    st.write("Name: {}" . format (name.upper()))

if st.button("Submit", key = 'new02') :
    st.write("Name: {}" . format (name.lower()))

# working with RADIObuttons
status = st.radio (" What is your status", ("Active" , "Inactive"))
if status == 'Active' :
    st.success("You are active")
elif status == "Inactive" :
    st.warning("Inactive")

# working with Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing something")

# working with Beta Expender 
if st.beta_expander("Python") :
    st.success("Hello Python")

with st.beta_expander ("JUlia") :
    st.text("hello julia")


