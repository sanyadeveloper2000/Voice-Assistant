import pyttsx3
import speech_recognition as sr
import wikipedia 
import datetime
import webbrowser
import os
import smtplib

print("Initializing Jarvis")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')



def speak(audio): #speak the text sent
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
       speak("Good Morning")
    elif(hour>=12 and hour<=18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi I am Jarvis. How may I help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening")
         r.pause_threshold=1
         audio=r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query
if __name__ == "__main__":
        wishme()
        while True:
            query=takecommand().lower()
            if 'wikipedia' in query:
                speak("Searching Wikipedia")
                query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            if 'open youtube' in query:
                webbrowser.open("youtube.com")
            if 'open google' in query:
                webbrowser.open("google.com")
            if  'open leetcode' in query:
                webbrowser.open("leetcode.com")
            if 'time' in query:
                T=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {T}")
            if 'work' in query:
                path=r"C:\\Users\\SANYA\\Desktop\\work"
                speak("Opening the folder")
                os.startfile(path)
            if 'quit' in query:
                speak("Bye, See you next time!")
                exit()
            else:
                 speak("Sorry I could not understand")


            
                   

 
   
    

