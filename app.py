import streamlit as st
from transformers import pipeline

st.title("AI Story Generator by Sudheer")

story_generator = pipeline('text-generation', model='gpt2')

prompt = st.text_input("Enter your story prompt:", "A lonely robot explores Jupiter's moon")

if st.button("Generate"):
    story = story_generator(prompt, max_length=150)[0]['generated_text']
    st.write("### Generated Story:")
    st.write(story)