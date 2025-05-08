import openai
from intent_classifier import process_input
from voice_module import listen_for_input, speak_with_eleven_labs
from spotify_integration import play_spotify_song
from weather_integration import get_weather
from reminder_integration import set_reminder
from utils import play_sound
import os
from dotenv import load_dotenv
import time

load_dotenv()
openai.api_key = os.getenv("your_openai_api_key")  

def main():
    while True:
        user_input = listen_for_input()
        if user_input:
            intent = process_input(user_input)
            if intent == 'greet':
                speak_with_eleven_labs("Hello!Anshul  How can I assist you today?I am Nivaan Your personal assistant")
            elif intent == 'play_music':
                speak_with_eleven_labs("Playing your requested music.")
                play_spotify_song("Your song name")  #
            elif intent == 'get_weather':
                weather = get_weather()
                speak_with_eleven_labs(weather)
            elif intent == 'set_reminder':
                set_reminder("Drink water", 3600)
            elif intent == 'get_time':
                speak_with_eleven_labs(f"The current time is {time.ctime()}")
            elif intent == 'shutdown':
                speak_with_eleven_labs("Shutting down the system.")
                os.system("shutdown /s /t 1")

            elif intent=='stress':
                  speak_with_eleven_labs("  I'm really sorry to hear that you're feeling so stressed. Life can get overwhelming sometimes, and it's completely okay to feel this way. Remember, you're not alone-many people experience stress, and it's important to acknowledge your feelings rather than bottle them up If you'd like, I can offer some strategies to help you manage your stress")
            
            elif intent=='Introduce':
                speak_with_eleven_labs(f"I am nivaan .I was made yesterday and i have got my name from two names that is Hridhaan and Nived")
            else:
                speak_with_eleven_labs("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()