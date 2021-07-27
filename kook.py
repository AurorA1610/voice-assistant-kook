'''voice assistant KOOK '''
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import subprocess
import smtplib
import socket

listener = sr.Recognizer()
kook = pyttsx3.init()

def talk(text):
    kook.say(text)
    kook.runAndWait()

def take_command():
    #global command
    try:
        with sr.Microphone() as source:
            print("Clearing background noises.. Please wait.")
            listener.adjust_for_ambient_noise(source,duration=0.5)
            print("I'm listening. Please speak..")
            voice =  listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()         
    except:
        pass
    return command

def WishMe():
    hr=int(datetime.datetime.now().hour)
    if hr>=0 and hr<=12:
        talk("Good Morning")
    elif hr>=12 and hr<=18:
        talk("Good Afternoon")
    else:
        talk("Good evening")
        
def sendEmail(to, content):
    addr = smtplib.SMTP('smtp.gmail.com',587)
    addr.ehlo()
    addr.starttls()
    f = open("Password.txt" '''the file in which you have kept the password of your email account''' , "r")
    a=f.read()
    addr.login('xyz@gmail.com' '''your email address''' , a)
    addr.sendmail('xyz@gmail.com' '''your email address''' , to, content)
    addr.close()

def run_kook():
    command = take_command()
    if 'hello' in command:                                                     #1. tell him hello
        talk('Hello!')
    elif 'who are you' in command:                                             #2. ask him his identity
        talk('I am Kook. Your Virtual Voice Assistant. Tell me how may I help you?')
    elif 'how are you' in command:                                             #3. ask him how he is 
        talk('I am pretty good. Thank you for asking.')
    elif 'time' in command:                                                    #4. know the current time
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:                                                    #5. play songs on youtube
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:                                           #5. search in wikipedia  
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        talk(info)
    elif'joke' in command:                                                     #6. enjoy a joke
        talk(pyjokes.get_joke())
    elif 'chrome' in command:                                                  #7. tell him to open chrome
        kook.say('Opening Chrome..')
        prog="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([prog])
    elif 'date' in command:
        talk('Sorry. I am way too busy.')                        #8. ask him on a date
    elif 'single' in command:
        talk('No. I am not single. i am in a relationship with Alexa.')  #9. ask him if he is single
    elif 'email to my dad' in command:                                         #10. ask him to send email
        try:
            talk("What should I say?")
            content = take_command()
            to = "pqr@gmail.com" '''receiver's email'''
            sendEmail(to, content)
            talk("Email has been sent")
        except socket.gaierror:
            print('ignoring failed address lookup')
            talk("Sorry, I was unable to send the email.")
    else:
        talk('Sorry. I did not get you. Guess I have to search it on internet for you.') #11. you talk rubbish
        pywhatkit.search(command)
        
        
WishMe()        
while True:
    run_kook()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    