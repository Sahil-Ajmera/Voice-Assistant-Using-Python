import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random
import sys
import datetime
import wikipedia

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

def open_youtube():
	chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
	webbrowser.get('chrome').open_new('youtube.com')

def open_google():
	chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
	webbrowser.get('chrome').open_new('google.com')	

def show_mycourses():
	path = "D:\\"
	os.startfile(path)

def open_mycourses():
	chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
	webbrowser.get('chrome').open_new('mycourses.rit.edu')

def open_linkedin():
	chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
	webbrowser.get('chrome').open_new('linkedin.com')

def open_sis():
	chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
	webbrowser.get('chrome').open_new('sis.rit.edu')

def open_github():
	chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
	webbrowser.get('chrome').open_new('github.com')

def open_tigercenter():
	chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
	webbrowser.get('chrome').open_new('tigercenter.rit.edu')

def open_gmail():
	chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
	webbrowser.get('chrome').open_new('gmail.com')

def play_music_offline():
	music_dir = 'D:\\songs'
	songs = os.listdir(music_dir)
	songnumber = random.randint(0,len(songs))
	os.startfile(os.path.join(music_dir,songs[songnumber]))

def open_sublime_text():
	path = "D:\\Program Files\\Sublime Text 3\\sublime_text.exe"
	os.startfile(path)

def open_intelliJ():
	path = "D:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2017.3\\bin\\idea64.exe"
	os.startfile(path)

def open_pycharm():
	path = "D:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1\\bin\\pycharm64.exe"
	os.startfile(path)

def open_cmd():
	os.system("start cmd.exe")

def current_day():
	dict = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
	speak("It is "+dict[datetime.datetime.today().weekday()])

def current_date():
	strtime = datetime.datetime.now().strftime("%d-%B-%Y")
	speak(f"Sir , Today's date is {strtime}")

def current_time():
	strtime = datetime.datetime.now().strftime("%H:%M:%S")
	speak(f"Sir , the current time is {strtime}")

def search_wikipedia(query):
	results = wikipedia.summary(query, sentences=2)
	speak("According to Wikipedia")
	speak(results)

def mute():
	speak('From now on, I will let you focus sir.')

def shutdown():
	sys.exit()

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
				open_youtube()
			elif 'open google' in query or 'open google.com' in query:
				open_google()
			elif 'show my courses' in query:
				show_mycourses()
			elif 'open my courses' in query or 'mycourses' in query or 'my courses' in query:
				open_mycourses()
			elif 'open linkedin' in query or 'linkedin' in query:
				open_linkedin()
			elif 'open sis' in query or 'sis' in query:
				open_sis()
			elif 'open github' in query or 'github' in query:
				open_github()
			elif 'open tigercenter' in query or 'tigercenter' in query:
				open_tigercenter()
			elif 'show me my emails' in query or 'gmail' in query:
				open_gmail()
			elif 'music' in query or 'song' in query or 'play anything' in query:
				play_music_offline()
			elif 'open sublime text' in query or 'open sublime' in query:
				open_sublime_text()
			elif 'open intellij' in query or 'intellij' in query:
				open_intelliJ()
			elif 'open pycharm' in query or 'pycharm' in query:
				open_pycharm()
			elif 'open cmd' in query or 'cmd' in query:
				open_cmd()
			elif 'shut up' in query or 'take a break' in query or 'mute yourself' in query:
				mute()
				listen = False
			elif 'shut down' in query or 'exit' in query:
				shutdown()
			elif 'time' in query:
				current_time()
			elif 'date' in query:
				current_date()
			elif 'day' in query:
				current_day()
			elif 'wikipedia' in query or 'who is' in query or 'what is' in query:
				query = query.replace("wikipedia", "")
				if len(query) < 0:
					continue
				search_wikipedia(query)
			else:
				speak('Sorry sir. Can you repeat that?')

		if 'are you there' in query or 'jarvis' in query and listen == False:
			speak("At your service sir")
			listen = True






if __name__=="__main__":
	main()