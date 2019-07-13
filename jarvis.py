import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def takeCommand():
	'''
	Takes microphone input from the user and return string output
	'''
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening ...")
		r.pause_threshold = 2
		audio = r.listen(source)

	try:
		print("Recognizing")
		query = r.recognize_google(audio, language='en-in')
		print("Query: "+query)
	except Exception as e:
		#print(e)
		#speak("Sir I did not get that.")
		return "None"
	return query

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
	while True:
		query = takeCommand().lower()
		'''
		Define Tasks
		# Mute Jarvis
		# Bring back Jarvis
		# Search videos on youtube
		# Search for something on wikipedia
		# Calculate something
		# Open a sublime text editor
		# Open a file explorer for summer classes files
		# Play music online
		# Play music offline
		# Open Youtube
		# Open Google
		# Search results for google 
		'''
		if 'open youtube' in query or 'open youtube.com' in query:
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open_new('youtube.com')
		elif 'open google' in query or 'open google.com' in query:
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open_new('google.com')
		elif 'music' in query or 'song' in query or 'play anything' in query:
			music_dir = 'D:\\songs'
			songs = os.listdir(music_dir)
			songnumber = random.randint(0,len(songs))
			os.startfile(os.path.join(music_dir,songs[songnumber]))
		elif 'open sublime text' in query or 'open sublime' in query:
			path = "D:\\Program Files\\Sublime Text 3\\sublime_text.exe"
			os.startfile(path)




if __name__=="__main__":
	main()