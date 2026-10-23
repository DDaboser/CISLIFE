import streamlit as st

# Home Page Title and Welcome
st.title("Welcome to CISLife!")

# User inputs for First and Last Name
first_name = st.text_input("Please enter your FIRST name:")
last_name = st.text_input("Please enter your LAST name:")

if first_name and last_name:
  st.write(f"Hello, {first_name} {last_name}! Welcome to CISLife!")

# Grade selection
grade = st.selectbox(
    "Please select the grade you want to be in:", ["Select a grade", "9"]
)

if grade == "9":
  st.success("Welcome to the 9th grade!")

  # Define the class sets
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

  # Display the set options
  st.write("### Available Class Sets:")
  st.write("**Set 1:**", ", ".join(set1))
  st.write("**Set 2:**", ", ".join(set2))

  # User selection for Set 1 or Set 2
  selected_set = st.radio(
      "Please select your 8 classes for the 9th grade:",
      ["Set 1", "Set 2"],
      index=None,  # No set selected by default
  )

  # Display confirmation based on choice
  if selected_set == "Set 1":
    st.info(f"You have selected **Set 1**: {', '.join(set1)}")
  elif selected_set == "Set 2":
    st.info(f"You have selected **Set 2**: {', '.join(set2)}")
    

    
