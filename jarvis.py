import pyttsx3
import speech_recognition as sr
import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User: {query}\n")
        return query
    except Exception as e:
        print(e)
        return ""

def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I assist you today?")

if __name__ == "__main__":
    wish_user()

    while True:
        query = listen().lower()

        if "exit" in query:
            speak("Goodbye!")
            break

        if "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        import pyttsx3
import speech_recognition as sr
import datetime
import requests
import json

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User: {query}\n")
        return query
    except Exception as e:
        print(e)
        return ""

def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I assist you today?")

def get_weather(city_name):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = json.loads(response.text)
    if weather_data["cod"] == "404":
        return "City not found. Please try again."
    else:
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        return f"Currently, it's {description} with a temperature of {temperature}°C and {humidity}% humidity in {city_name}."

if __name__ == "__main__":
    wish_user()

    while True:
        query = listen().lower()

        if "exit" in query:
            speak("Goodbye!")
            break

        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif "weather" in query:
            speak("Sure, please tell me the city name.")
            city_name = listen()
            weather_info = get_weather(city_name)
            speak(weather_info)

        elif "news" in query:
            api_key = "YOUR_NEWSAPI_API_KEY"
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
            response = requests.get(url)
            news_data = json.loads(response.text)
            articles = news_data["articles"][:5]  # Get the top 5 headlines
            speak("Here are the top 5 news headlines.")
            for idx, article in enumerate(articles):
                speak(f"Headline {idx+1}: {article['title']}")

        # Add more functionalities based on user input


    





