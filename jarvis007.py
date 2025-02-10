from __future__ import with_statement
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sameer!")
        print("Good Morning sameer!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sameer!")
        print("Good Afternoon sameer!")
    else:
        speak("Good Evening Sameer!")
        print("Good Evening Sameer!")
        
    speak("What can I do for you?")
    print("What can I do for you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"S.I.F.R.A: {query}\n")

    except sr.UnknownValueError:
        print("Could not understand the audio")
        return "None"
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return "None"
    return query
        
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

#wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

#time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

#conversation
        elif "who are you" in query:
            print('My Name Is SIFRA')
            speak('My Name Is SIFRA')
            print('I can Do Everything that my sameer programmed me to do')
            speak('I can Do Everything that my sameer programmed me to do')

        elif "who created you" in query:
            print('Mohammed Sameer and his firends  created me and I was created with Python Language, in Visual Studio Code.')
            speak('Mohammed Sameer and his friends created me and I was created with Python Language, in Visual Studio Code.')
        
        elif "i love you" in query:
            print('really ? i was waiting for this day ! i love you too !')
            speak('really ? i was waiting for this day ! i love you too !')

        elif "bhojraj" in query:
            speak('Bhoojraj is a fat ass boy')

        elif "bharat" in query:
            speak('bharat is a gen du boy')
#notepad
        elif "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe" 
            os.startfile(npath)

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

#command prompt
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

#youtube
        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'open youtube' in query:
            speak("What would you like to watch?")
            qrry = takeCommand().lower()
            kit.playonyt(f"{qrry}")

        elif 'close youtube' in query:
            os.system("taskkill /f /im brave.exe")

#google(search problem)---
        elif 'open google' in query:
            speak("What should I search?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)

        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe")

#music
        elif 'play music' in query:
            music_dir = 'C:\\Users\\samee\\OneDrive\\Desktop\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'close music' in query:
            os.system("taskkill /f /im vlc.exe")

#screenshot
        elif "take screenshot" in query:
            speak('Tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot saved")

#calculater
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Ready")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)

            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.__truediv__,
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1, op2 = float(op1), float(op2)
                return get_operator_fn(oper)(op1, op2)

            speak("Your result is")
            speak(eval_binary_expr(*(my_string.split())))

#ip address
        elif "what is my ip address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("Your IP address is")
                speak(ipAdd)
            except Exception as e:
                speak("Network is weak, please try again some time later")

#volume
        elif "volume up" in query:
            for _ in range(15):
                pyautogui.press("volumeup")

        elif "volume down" in query:
            for _ in range(15):
                pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

#scroll 
        elif "scroll up" in query:
            pyautogui.scroll(1000)

        elif "scroll down" in query:
            pyautogui.scroll(-1000)

#move application ----audio
        elif "drag google play to the right" in query:
            pyautogui.moveTo(46, 31, 2)
            pyautogui.dragRel(1857, 31, 2)

#paint
        elif "rectangular spiral" in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('paint')
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.moveTo(100, 193, 1)
            pyautogui.rightClick
            pyautogui.click()
            distance = 300
            while distance > 0:
                pyautogui.dragRel(distance, 0, 0.1, button="left")
                distance -= 10
                pyautogui.dragRel(0, distance, 0.1, button="left")
                pyautogui.dragRel(-distance, 0, 0.1, button="left")
                distance -= 10
                pyautogui.dragRel(0, -distance, 0.1, button="left")

        elif "close paint" in query:
            os.system("taskkill /f /im mspaint.exe")

#crome
        elif 'open chrome' in query:
            os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        elif 'maximize this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
        elif 'youtube search' in query:
            query = query.replace("youtube search", "")
            pyautogui.hotkey('alt', 'd')
            time.sleep(1)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')
        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')
        elif 'minimise this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')
        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')
        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')
        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        elif 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
        elif 'close window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'w')
        elif 'clear chrome history' in query:
            pyautogui.hotkey('ctrl', 'shift', 'delete')
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

#typeing
        elif 'type' in query: #10
            query = query.replace("type", "")
            pyautogui.write(f"{query}")

#stop program
        elif "go to sleep" in query:
            speak('Alright then, I am switching off')
            sys.exit()

        elif "bye-bye" in query:
            speak('Alright then, keep smiling')
            sys.exit()

        elif "chala ja" in query:
            speak('teek hayy')
            sys.exit()

#close code
        elif "close vs code" in query:
            speak("okey bye")
            os.system("taskkill /f /im code.exe")

#camera (problem: it will not close once its open)
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(5)
                if k == 3:
                    break
            cap.release()
            cv2.destroyAllWindows()

#system 
        elif "shut down" in query:
            os.system("shutdown /s /t 5")

        elif "restart" in query:
            os.system("shutdown /r /t 5")

        elif "lock" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "refresh" in query:
            pyautogui.moveTo(1551, 551, 2)
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620, 667, 1)
            pyautogui.click(x=1620, y=650, clicks=1, interval=0, button='left')





