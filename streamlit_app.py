import streamlit as st
import random

st.set_page_config(page_title="Role–Goal–Style Cards", layout="centered")

st.title("🎴 Role • Goal • Style")

roles = [
    "Kindergarten teacher",
    "Rapper",
    "Two-year-old",
    "Computer scientist",
    "Very sad person",
    "Artist"
]

goals = [
    "Give instructions to build a paper airplane",
    "Give five dinner ideas (20 minutes)",
    "Translate a sentence into French",
    "Write a birthday card",
    "Write Python code to add two numbers",
    "Recommend things to do in New York City",
    "Teach a card game",
    "List books about rainforests"
]

styles = [
    "As a poem",
    "In the style of Shakespeare",
    "With emojis only",
    "With as many puns as possible",
    "In one sentence",
    "With formal language",
    "In a pirate voice"
]

if "role" not in st.session_state:
    st.session_state.role = "—"
    st.session_state.goal = "—"
    st.session_state.style = "—"

if st.button("🎲 Draw cards"):
    st.session_state.role = random.choice(roles)
    st.session_state.goal = random.choice(goals)
    st.session_state.style = random.choice(styles)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🟦 ROLE")
    st.markdown(
        f"<div style='padding:20px; border:2px solid #4F8BF9; border-radius:12px; text-align:center; font-size:18px;'>"
        f"{st.session_state.role}</div>",
        unsafe_allow_html=True
    )

with col2:
    st.markdown("### 🟩 GOAL")
    st.markdown(
        f"<div style='padding:20px; border:2px solid #3CB371; border-radius:12px; text-align:center; font-size:18px;'>"
        f"{st.session_state.goal}</div>",
        unsafe_allow_html=True
    )

with col3:
    st.markdown("### 🟨 STYLE")
    st.markdown(
        f"<div style='padding:20px; border:2px solid #F4C430; border-radius:12px; text-align:center; font-size:18px;'>"
        f"{st.session_state.style}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")
st.markdown("✍️ **Student task:** Combine the three cards into your own prompt.")
