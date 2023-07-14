#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "当前时间:" + time.asctime(t)
 
print(str);
import streamlit as st
from transformers import pipeline

# Load chat GLM2-6B model
model_path = "path/to/chat_glm2_6b"
chatbot = pipeline("text-generation", model=model_path, tokenizer=model_path)

# Define form inputs
name = st.text_input("What is your name?")
age = st.slider("How old are you?", 1, 100)
hobbies = st.text_input("What are your hobbies?")

# Define personalized prompts and responses
prompts = {
    "greeting": f"Hi, my name is {name}. I am {age} years old, and I like {hobbies}.",
    "question": "Can you tell me more about that?",
    "goodbye": "Nice talking to you. Goodbye!"
}
responses = {
    "greeting": "Hello! It's nice to meet you.",
    "question": "Sure, I'd be happy to.",
    "goodbye": "Goodbye! Have a great day."
}

# Define conversation state
state = {
    "stage": "greeting",
    "context": ""
}

# Generate personalized response based on user input
def generate_response(input_text, state):
    try:
        prompt = prompts[state["stage"]] + state["context"] + input_text
        response = chatbot(prompt, max_length=50)[0]['generated_text']
        state["context"] = response
        if state["stage"] == "goodbye":
            state["stage"] = "greeting"
            state["context"] = ""
        else:
            state["stage"] = "question"
        return response
    except Exception as e:
        st.write(f"Error: {e}")

# Define streamlit app
def app():
    st.set_page_config(page_title="Personalized Chatbot", page_icon=":robot_face:")
    st.title("Personalized Chatbot")
    st.write("Please enter some information about yourself:")
    user_input = st.text_input("Input:")
    if user_input:
        response = generate_response(user_input, state)
        st.write("Output:")
        st.write(responses[state["stage"]] + response)
    st.write("---")
    st.write("Debugging Information:")
    st.write(f"Stage: {state['stage']}")
    st.write(f"Context: {state['context']}")

# Run streamlit app
if __name__ == "__main__":
    app()
