import streamlit as st
import speech_recognition as sr

# Streamlit App Title
st.title("🎙️ Voice to Text Converter")

# Initialize the Recognizer
recognizer = sr.Recognizer()

# Button to Start Recording
if st.button("Start Recording"):
    try:
        # Use Microphone as Source
        with sr.Microphone() as source:
            st.info("🎧 Listening... Please speak clearly.")
            recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
            audio = recognizer.listen(source)

        # Convert Speech to Text using Google Speech Recognition
        try:
            text = recognizer.recognize_google(audio)
            st.success("✅ Recognized Text:")
            st.write(text)
        except sr.UnknownValueError:
            st.error("❌ Could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"⚠️ Could not request results from Google Speech Recognition service; {e}")

    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")


