import speech_recognition as sr
import gtts
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager

intent_map = {
    "open youtube": "youtube",
    "hello": "hello",
}

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text.lower())
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None

def speak(text):
    sound = gtts.gTTS(text=text, lang="en")
    sound.save("welcome.mp3")
    playsound("welcome.mp3")

def process_intent(text):
    intent = intent_map.get(text.lower())  # Match entire lowercased text
    return intent

while True:
    user_choice = input("Enter 'speak' for speech recognition or 'type' to enter text: ").lower()
    if user_choice == "speak":
        user_input = recognize_speech()
    elif user_choice == "type":
        try:
            user_input = input("Enter your text: ").lower()
        except KeyboardInterrupt:
            print("\nExiting program...")
            break
    else:
        print("Invalid choice. Please enter 'speak' or 'type'.")
        continue

    intent = process_intent(user_input)

    if user_input:
        if intent == "hello":
            response = "Hello sir! How can I help you today?"
            speak(response)  # Now response is defined within the same indentation level

        elif intent == "youtube":
            try:
                speak("Opening YouTube")
                options = Options()
                options.add_experimental_option("detach", True)

                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                driver.get("https://www.youtube.com/")
                driver.maximize_window()
            except Exception as e:
                print(f"An error occurred while opening YouTube: {e}")
                speak("Sorry, I couldn't open YouTube at this time.")

        else:
            response = f"Hi there! You said: {user_input}"
            speak(response)
    else:
        print("No input received.")
