import streamlit as st
import pandas as pd

# Load student data from Excel file
try:
    student_df = pd.read_excel("student_data.xlsx")
except FileNotFoundError:
    student_df = pd.DataFrame(columns=["Name", "Marks"])

# Function to add a new student to the DataFrame and Excel file
def add_student(name, marks):
    new_student = pd.DataFrame([[name, marks]], columns=["Name", "Marks"])
    student_df = student_df.append(new_student, ignore_index=True)
    student_df.to_excel("student_data.xlsx", index=False)

# Function to check admission criteria
def check_admission(student_name):
    student_row = student_df.loc[student_df["Name"] == student_name]
    if not student_row.empty:
        marks = student_row.iloc[0]["Marks"]
        if marks >= 75:
            return f"{student_name} is admitted!"
        else:
            return f"{student_name} does not meet admission criteria."
    else:
        return f"{student_name} is not found in the database."

# Streamlit UI
st.title('Education System')

# Add new student form
st.subheader('Add New Student')
new_student_name = st.text_input('Enter student name:')
new_student_marks = st.number_input('Enter student marks:', min_value=0, max_value=100)

if st.button('Add Student'):
    add_student(new_student_name, new_student_marks)
    st.success(f'{new_student_name} added successfully!')

# View existing students and marks
st.subheader('Existing Students and Marks')
st.write(student_df)

# Chatbot interface
st.subheader('Chat with EducationBot')
user_input = st.text_input('You:')

if st.button('Send'):
    response = "I'm sorry, I didn't understand that."
    st.write('EducationBot:', response)

# Admission checker
st.subheader('Admission Checker')
admission_student = st.text_input('Enter student name to check admission:')
if st.button('Check Admission'):
    admission_result = check_admission(admission_student)
    st.write(admission_result)
