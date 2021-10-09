import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer, QTime, QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis import Ui_MainWindow





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty("voices",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:    
        speak("good morning !")

    elif hour>=12 and hour<18:
        speak("good afternoon !")

    else:
        speak("good evening !") 

    speak("I am jarvis sir. please tell me how may I help U ")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to ,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mohamedfaraaz007@gmail.com','faraaz007')
    server.sendmail("mohamedfaraaz007@gmial.com", to, content)
    server.close()

class Mainthread(Qthread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

startExecution = Mainthread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:\\pics\\7LP8.gif")
        self.ui.lable.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:\\pics\\Jarvis_Loading_Screen.gif")
        self.ui.lable_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()



    def showTime(self):
        current_time = QTime.currentTime()
        current = QDate.currentDate()
        label_time = current_time.tostring('hh:mm:ss')
        label_date = current.tostring(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.execute)



if __name__ == "__main__":
    WishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching WikiPedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak( "According to Wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open('youtube.com')    

        elif "open google" in query:
            webbrowser.open('google.com') 

        elif "open stackoverflow" in query:
            webbrowser.open('stackoverflow.com')

        elif "play music" in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))
        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir the time is {strTime}")
      
        elif "open code" in query:
            codepath = "C:\\Users\\Faraaz\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


        elif 'email to france' or 'home' in query:
            try:
                speak("what should I say sir?")
                content = takecommand()
                to = "mohamedfaraaz007@gmail.com"
                sendEmail(to,content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("sorry faraaz bhai your email I am not able to send")