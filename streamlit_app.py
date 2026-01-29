import streamlit as st
import random

st.set_page_config(page_title="Prompt Card Generator", layout="centered")

st.title("🎴 AI Prompt Card Generator")
st.write("Draw one **Role**, one **Goal**, and one **Style** to build a creative prompt!")

# ----- Decks -----
roles = [
    "Kindergarten teacher",
    "Rapper",
    "Personal tutor",
    "Two-year-old",
    "Government regulator",
    "Computer scientist",
    "Very sad person",
    "Artist"
]

goals = [
    "Give me instructions on how to build a paper airplane",
    "Give me five dinner ideas that can be made in 20 minutes",
    "Translate this sentence into French",
    "Write a birthday card to my friend",
    "Write code in Python to add two numbers together",
    "Give 5 recommendations for what to do on my trip to New York City",
    "Teach me how to play a card game",
    "Give me a list of books about rainforests"
]

styles = [
    "As an acrostic poem",
    "In the style of Shakespeare",
    "In emojis only",
    "With as many puns as possible",
    "In one sentence",
    "In fewer than 30 words",
    "With formal language",
    "In a pirate voice"
]

# ----- Button -----
if st.button("🎲 Draw cards"):
    role = random.choice(roles)
    goal = random.choice(goals)
    style = random.choice(styles)

    st.subheader("🧩 Your Prompt")
    prompt = f"""
    You are a **{role}**.
    
    **Task:** {goal}
    
    **Style:** {style}
    """
    st.markdown(prompt)

    st.info("👉 Copy this prompt and paste it into ChatGPT!")
