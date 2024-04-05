import speech_recognition as sr
from gtts import gTTS

# Speech recognition function
def recognize_speech():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

  try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
    if text == "type":
        speak(text)
    return text
  except sr.UnknownValueError:
    print("Could not understand audio")
    return None
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return None

# Text-to-speech function using gTTS
def speak(text):
  tts = gTTS(text=text, lang='en')
  tts.save("output.mp3")
  

# Main loop
while True:
  user_input = recognize_speech()
  if user_input == "type":


    # Example response (replace with your actual logic)
    response = f"Hi there! You said: {user_input}"
    speak(response) 

