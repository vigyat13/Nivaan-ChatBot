import speech_recognition as sr
from elevenlabs import generate, play, set_api_key


set_api_key("elevenlabs_api_key")  

def listen_for_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio)
        print(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None

def speak_with_eleven_labs(text):
    try:
        audio = generate(
            text=text,
            voice="Charlie"  
        )
        play(audio)
    except Exception as e:
        print("Error generating or playing audio:", e)
