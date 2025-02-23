import streamlit as st
import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

def recognize_speech_from_microphone(is_listening=True):
    # Use the microphone as the source for audio input
    with sr.Microphone() as source:
        while is_listening:
            st.write("🎧 Listening... Please speak clearly.")
            recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
            audio = recognizer.listen(source)  # Listen for the first phrase
            
            try:
                # Recognize speech using Google's Speech Recognition API
                text = recognizer.recognize_google(audio)
                return text  # Return the transcribed text
                
            except sr.UnknownValueError:
                st.error("Google Speech Recognition could not understand the audio")
            except sr.RequestError as e:
                st.error(f"Could not request results from Google Speech Recognition service; {e}")

# Streamlit UI Logic
st.title("🎙️ Voice to Text Converter")

# Button to start recording
if st.button("Start Recording"):
    recognized_text = recognize_speech_from_microphone()
    if recognized_text:
        st.success("✅ Recognized Text:")
        st.write(recognized_text)
