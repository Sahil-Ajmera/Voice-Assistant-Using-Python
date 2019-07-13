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

def wishMe():
	'''
	Wishes user
	'''
	hour = int(datetime.datetime.now().hour)

	if hour>=0 and hour<12:
		speak("Good Morning sir. Jarvis at your service")

	elif hour>=12 and hour<18:
		speak("Good Afternoon sir. Jarvis at your service")

	else:
		speak("Good Evening sir. Jarvis at your service")

def main():
	wishMe()
	
if __name__=="__main__":
	main()