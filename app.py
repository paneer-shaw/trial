import streamlit as st
import azure.cognitiveservices.speech as speechsdk
import pyodbc
import pandas as pd
from datetime import datetime

#FBFBFA
st.markdown(
    """
    <style>
    .main {
        background-color: #FBFBFA;
    }
    .banner {
        background-color: #014149; 
        color: white; 
        text-align: center; 
        font-size: 24px; 
        font-family: 'Helvetica',sans-serif;
        font-weight: bold; 
        border-radius: 8px; 
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="banner">ClearDysarthric</div>', unsafe_allow_html=True)
st.write("We aim to help people with dysarthria communicate.")
st.subheader('Project Objectives')
st.markdown("""
            - Helping people understand dysarthric speech
            - Using cloud services
            - Building a user-friendly, assistive tech that allows accessibility""")


"""def insert_user(name, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, created_at) VALUES (?, ?, ?)", (name, email, datetime.now()))
    conn.commit()
    conn.close()

st.markdown("### Join Our Mailing List", unsafe_allow_html=True)
st.write("Sign up to receive our newsletter!")

# Input fields for name and email
name = st.text_input("Your Name", placeholder="Enter your name here")
email = st.text_input("Your Email", placeholder="Enter your email here")

# Submission button
if st.button("Submit"):
    if name and email:
        insert_user(name, email)
        st.success("Thank you for signing up!")
    else:
        st.error("Please fill in both your name and email.")

def speech_to_text():
    speech_config = speechsdk.SpeechConfig(subscription="<your_azure_subscription_key>", region="<your_region>")
    audio_input = speechsdk.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    
    st.write("Say something...")
    result = recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        st.write("Recognized: {}".format(result.text))
    else:
        st.write("No speech recognized")
if st.button("Record Speech"):
    speech_to_text()"""