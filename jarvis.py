import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def main():
	speak("Hi Sir. Jarvis at your service")

if __name__=="__main__":
	main()