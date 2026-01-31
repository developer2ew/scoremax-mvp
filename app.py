import streamlit as st

st.set_page_config(
    page_title="ScoreMax – UPSC Prelims",
    layout="centered"
)

st.title("ScoreMax")
st.subheader("UPSC Prelims GS Paper-I Decision Assistant")

st.markdown("---")

st.markdown("### Step 1: Paste the Question (optional)")
question = st.text_area(
    "You may paste the MCQ here for context (not analyzed yet)"
)

st.markdown("### Step 2: Your Self-Assessment")

familiarity = st.selectbox(
    "How familiar are you with this topic?",
    ["High", "Medium", "Low"]
)

elimination = st.slider(
    "How many options can you confidently eliminate?",
    0, 3, 0
)

risk = st.selectbox(
    "Your risk appetite for this attempt?",
    ["Conservative", "Balanced", "Aggressive"]
)

st.markdown("---")

if st.button("Get Decision"):
    decision = ""
    explanation = ""

    if familiarity == "Low" and elimination <= 1:
        decision = "❌ SKIP"
        explanation = "Low familiarity and weak elimination increases negative marking risk."

    elif elimination == 3:
        decision = "✅ ATTEMPT"
        explanation = "With 3 options eliminated, probability is strongly in your favor."

    elif familiarity == "High" and elimination >= 2:
        decision = "✅ ATTEMPT"
        explanation = "Strong conceptual clarity with solid elimination."

    elif familiarity == "Medium" and elimination == 2:
        if risk == "Conservative":
            decision = "⚠️ SKIP"
            explanation = "Balanced probability, but conservative strategy suggests skipping."
        else:
            decision = "✅ ATTEMPT"
            explanation = "Calculated risk acceptable with 2 eliminations."

    else:
        decision = "⚠️ BORDERLINE"
        explanation = "Decision depends on exam pressure and overall attempts."

    st.markdown("## Decision")
    st.success(decision)

    st.markdown("### Why?")
    st.write(explanation)

    st.markdown("---")
    st.caption("ScoreMax MVP – Decision logic inspired by UPSC Prelims strategy")
