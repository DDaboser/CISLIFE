import streamlit as st

# Home Page Title and Welcome Message
st.title("CISLife!")
st.write("Welcome to CISLife!")

# Getting user input for names
first_name = st.text_input("Please enter your FIRST name:")
last_name = st.text_input("Please enter your LAST name:")

if first_name and last_name:
  st.write(f"Hello, {first_name} {last_name}!")

st.write("Welcome to CISLife!")

# Grade selection using a dropdown (selectbox)
grade = st.selectbox("Please enter the grade you want to be in:", ["", "9"])

if grade == "9":
  st.success("Welcome to the 9th grade!")
  st.write(
      "Please select your 8 classes for the 9th grade by selecting one of these"
      " sets:"
  )

  set1 = [
      "English",
      "Math",
      "Science",
      "History",
      "PE",
      "Art",
      "Music",
      "Computer Science",
  ]
  set2 = [
      "English",
      "Math",
      "Science",
      "History",
      "PE",
      "Art",
      "Drama",
      "AP Computer Science",
  ]

  st.write("**Set 1:**", set1)
  st.write("**Set 2:**", set2)
    

    
