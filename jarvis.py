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
		r.pause_threshold = 1
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
	listen = True
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
		# Open Intellij
		# Open Pycharm
		# Open command prompt
		# Open a file explorer for summer classes files
		# Play music online
		# Play music offline
		# Open Youtube
		# Open Google
		# Open mycourses
		# Open sis
		# Open tigercenter
		# Open Github
		# Open gmail
		# Open linkedin
		# Search results for google 
		'''

		if listen != False:

			if 'open youtube' in query or 'open youtube.com' in query:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new('youtube.com')
			elif 'open google' in query or 'open google.com' in query:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new('google.com')
			elif 'show my courses' in query:
				path = "D:\\"
				os.startfile(path)
			elif 'open my courses' in query or 'mycourses' in query or 'my courses' in query:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new('mycourses.rit.edu')
			elif 'open linkedin' in query or 'linkedin' in query:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new('linkedin.com')
			elif 'open sis' in query or 'sis' in query:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new('sis.rit.edu')
			elif 'open github' in query or 'github' in query:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new('github.com')
			elif 'open tigercenter' in query or 'tigercenter' in query:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new('tigercenter.rit.edu')
			elif 'show me my emails' in query or 'gmail' in query:
				chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
				webbrowser.get('chrome').open_new('gmail.com')
			elif 'music' in query or 'song' in query or 'play anything' in query:
				music_dir = 'D:\\songs'
				songs = os.listdir(music_dir)
				songnumber = random.randint(0,len(songs))
				os.startfile(os.path.join(music_dir,songs[songnumber]))
			elif 'open sublime text' in query or 'open sublime' in query:
				path = "D:\\Program Files\\Sublime Text 3\\sublime_text.exe"
				os.startfile(path)
			elif 'open intellij' in query or 'intellij' in query:
				path = "D:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2017.3\\bin\\idea64.exe"
				os.startfile(path)
			elif 'open pycharm' in query or 'pycharm' in query:
				path = "D:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1\\bin\\pycharm64.exe"
				os.startfile(path)
			elif 'open cmd' in query or 'cmd' in query:
				os.system("start cmd.exe")
			elif 'shut up' in query or 'take a break' in query:
				speak('From now on, I will let you focus sir.')
				listen = False
			elif 'shutdown' in query or 'exit' in query:
				sys.exit()
			else:
				speak('Sorry sir. Can you repeat that?')

		if 'are you there' in query or 'jarvis' in query and listen == False:
			speak("At your service sir")
			listen = True






if __name__=="__main__":
	main()