import streamlit as st

st.set_page_config(
    page_title="ScoreMax – UPSC Prelims",
    page_icon="📘",
    layout="centered"
)

st.title("ScoreMax")
st.caption("UPSC Prelims Decision Assistant")

st.divider()

st.selectbox(
    "Exam",
    ["UPSC Prelims 2024", "UPSC Prelims 2025", "UPSC Prelims 2026"]
)
st.selectbox("Subject", ["Polity", "History", "Geography", "Economy"])
st.selectbox("Question Type", ["MCQ (Single correct)"])

st.text_area("Paste the UPSC-style question", height=120)

st.text_input("Option A")
st.text_input("Option B")
st.text_input("Option C")
st.text_input("Option D")

confidence = st.slider(
    "Your confidence level (0 = pure guess, 100 = almost sure)",
    0, 100, 50
)

st.divider()

if st.button("Analyze Risk & Best Choice"):
    st.subheader("Recommended Action")
    st.write("—")

    st.subheader("Risk Analysis")
    st.write("—")

    st.subheader("Why this option?")
    st.write("—")

st.divider()
st.caption("ScoreMax is an assistive decision tool. Final responsibility lies with the candidate.")