import webbrowser
import time
import pyttsx3
import pyautogui
import os
os.environ["ALSA_LOG_LEVEL"] = "none"
import speech_recognition as sr
import pyaudio
R=sr.Recognizer()
def listen():
   text=""
   with sr.Microphone()as source:
      print("listening...")
      audio=R.listen(source)
      text=R.recognize_google(audio)
      print("you said:"+text)
   return text
engine=pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()


choice =listen().lower()
if "google" in choice:
    say("open google")
    print("open google")
    say("what you want search on google:")
    topic = listen().lower()
    webbrowser.open("https://www.google.com/search?q=" + topic)
    time.sleep(4)
    pyautogui.moveTo(370, 370)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(1125, 435)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(1150, 435)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()

elif "youtube" in choice:
    say("open youtube")
    print("open youtube")
    say("what you want search on youtube:")
    topic = listen().lower()
    webbrowser.open("https://www.youtube.com/results?search_query=" + topic)
    time.sleep(4)
    pyautogui.moveTo(450, 650)
    pyautogui.click()
    pyautogui.moveTo(870, 640)
    time.sleep(20)
    pyautogui.click()
    