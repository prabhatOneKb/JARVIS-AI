import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices') 
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
def wishMe():
   hour=int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
    speak(" Good Morning!")
   elif hour>=12 and hour<18:
    speak("Good afternoon!")
   else:
    speak("Good evening!")
speak("hlo sir. i am subzero. please tell me how may i help you")

def takeCommand():
  #it takes voice input from the user and return string as a output..
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
      #print(e)
        print("say that again please..")
        return "None"
    return query
def sendEmail(to, content):
   server=smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.login('pratimabisoyi010176@gmail.com','your-password')
   server.sendmail('youremail@gmail.com',to,content)
   server.close()


      
if __name__=="__main__":
    wishMe()
    if 1:
    #while True:
        query= takeCommand().lower()
        #login for executing tasks based on query
        if 'wikipedia' in query:
           speak('searching wikipedia...')
           query=query.replace("wikipedia", "")
           results=wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           speak(results)
        elif 'open youtube' in query:
           webbrowser.open("youtube.com")
        elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
           music_dir='C:\\musicd'
           songs= os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))
         
        elif 'the time' in query:
           strTime=datetime.datetime.now().strftime("%h:%m:%s")
           speak(f"sir,the time is {strTime}")
        elif 'open code' in query:
           codePath="C:\\Users\\prabhat kumar bisoyi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
        elif 'email to prabhat' in query:
           try:
              speak("what should i mail?")
              content=takeCommand()
              to="pratimabisoyi010176@gmail.com"
              sendEmail(to, content)
              speak("successful!")
           except Exception as e:
              print(e)
              speak("sorry sir, due to some error i am unable to send this mail")
        elif 'quit' in query:
           exit