import streamlit as st
from utils import generate_answer  # This imports the function that generates the answer
from prompt_builder import build_prompt  # This imports the prompt-building function

# Streamlit app setup
st.title("Interview Cracker - AI Interview Assistant")

# User selects role, question type, tone, experience level, and location
role = st.selectbox("Select Role", ["Software Engineer","Scrum Master", "Data Scientist", "Project Manager"])
question_type = st.selectbox("Select Question Type", ["Behavioral", "Technical"])
tone = st.selectbox("Select Tone", ["Formal", "Casual", "Neutral"])
experience_level = st.selectbox("Select Experience Level", ["Junior", "Mid", "Senior"])
location = st.selectbox("Select Location To see Open Positions", ["Hyderabad", "Bangalore", "Chennai", "Hybrid", "Remote"])

question = st.text_input("Enter your question:")

# Add a submit button for generating answers
if st.button("Submit"):
    if question:
        # Build the prompt dynamically based on the user's inputs
        prompt = build_prompt(role, question_type, question, tone, experience_level)

        # Generate the answer using LangChain LLM
        response = generate_answer(prompt)

        # Display the answer to the user
        st.write(response)
    else:
        st.warning("Please enter a question!")

# Job openings search URL
def generate_linkedin_job_search_url(role, location):
    base_url = "https://www.linkedin.com/jobs/search/"
    query = f"?keywords={role.replace(' ', '%20')}&location={location.replace(' ', '%20')}"
    return base_url + query

# Display job search link
if st.button("Show Job Openings"):
    job_search_url = generate_linkedin_job_search_url(role, location)
    #st.write(f"[Click here to see job openings on LinkedIn]( {job_search_url} )")
    st.markdown(f'<a href="{job_search_url}" target="_blank">Click here to view job openings on LinkedIn</a>', unsafe_allow_html=True)
    st.stop()  # Stop further execution after redirecting
