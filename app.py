# app.py

import streamlit as st
from code_review import analyze_code

st.set_page_config(page_title="AI Code Reviewer", layout="centered")

st.title(" AI Code Reviewer")
st.write("Upload or paste your code and get instant feedback from an LLM!")

# User Input Options
upload_method = st.radio("Choose input method:", ["Paste Code", "Upload File"])

code_input = ""

if upload_method == "Paste Code":
    code_input = st.text_area("✏️ Paste your code here:", height=300)
elif upload_method == "Upload File":
    uploaded_file = st.file_uploader("📄 Upload a .py file", type=["py"])
    if uploaded_file is not None:
        code_input = uploaded_file.read().decode("utf-8")

# Button to review
if st.button("🔍 Review Code"):
    if not code_input.strip():
        st.warning("Please provide some code first.")
    else:
        with st.spinner("Analyzing your code with GPT..."):
            feedback = analyze_code(code_input)
            st.success("✅ Code Review Complete")
            st.markdown("### 📝 Feedback")
            st.markdown(feedback)
