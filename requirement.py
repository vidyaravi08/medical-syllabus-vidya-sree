import streamlit as st

# 1. App Setup
st.set_page_config(page_title="MedStudy Navigator", layout="wide")
st.title("🩺 MedStudy Navigator")

# 2. Syllabus Data Structure
syllabus = {
    "Cardiology": ["Heart Anatomy", "ECG Basics", "Hypertension"],
    "Neurology": ["Neuroanatomy", "Stroke Management", "Seizure Disorders"],
    "Pharmacology": ["Drug Classification", "Pharmacokinetics"]
}

# 3. Sidebar Navigation
subject = st.sidebar.selectbox("Select Subject", list(syllabus.keys()))
topic = st.sidebar.selectbox("Select Topic", syllabus[subject])

# 4. Main Content Area
st.header(f"{subject}: {topic}")

# Tab-based organization for better UX
tab1, tab2, tab3 = st.tabs(["Study Notes", "Active Recall", "Resources"])

with tab1:
    st.subheader("High-Yield Summary")
    st.write(f"Key facts and clinical pearls for {topic} go here...")
    
with tab2:
    st.subheader("Active Recall Quiz")
    if st.button("Show Question"):
        st.info("What is the primary mechanism of action for...?")
        
with tab3:
    st.subheader("Resources")
    st.link_button("View AMBOSS Library", "https://www.amboss.com")
