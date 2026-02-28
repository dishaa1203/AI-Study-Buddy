import streamlit as st

st.title("📚 AI-Powered Study Buddy")

# Topic input
topic = st.text_input("Enter study topic:")

# Explanation
if st.button("Explain Topic"):
    if topic:
        st.write("## Explanation")
        st.write(
            f"{topic} is a major field in computer science that focuses on creating intelligent machines "
            "that can perform tasks which normally require human intelligence. These tasks include learning "
            "from data, recognizing speech, understanding language, solving problems, and making decisions. "
            "AI uses techniques such as Machine Learning, Deep Learning, and Neural Networks. "
            "Examples of AI applications include virtual assistants like Alexa and Siri, recommendation systems "
            "like YouTube and Netflix, self-driving cars, chatbots, and medical diagnosis systems. "
            "AI helps improve efficiency, accuracy, and automation in many industries such as healthcare, education, "
            "banking, and transportation."
        )

# Quiz in proper MCQ format
if st.button("Generate Quiz"):
    if topic:
        st.write("## Quiz (MCQs)")
        
        st.write("**1. What is Artificial Intelligence?**")
        st.write("A) Human brain")
        st.write("B) Technology that simulates human intelligence")
        st.write("C) Hardware device")
        st.write("D) Operating system")
        st.write("**Answer: B**")
        
        st.write("---")
        
        st.write("**2. Which field is part of AI?**")
        st.write("A) Machine Learning")
        st.write("B) Civil Engineering")
        st.write("C) Mechanical Drawing")
        st.write("D) None")
        st.write("**Answer: A**")
        
        st.write("---")
        
        st.write("**3. Which is an example of AI?**")
        st.write("A) Calculator")
        st.write("B) Chatbot")
        st.write("C) Keyboard")
        st.write("D) Mouse")
        st.write("**Answer: B**")

# Notes summarize
notes = st.text_area("Paste notes to summarize:")

if st.button("Summarize Notes"):
    if notes:
        st.write("## Summary")
        words = notes.split()
        short = " ".join(words[:40])  # show first 40 words
        st.write(short + "...")
    else:
        st.write("Please paste notes first.")