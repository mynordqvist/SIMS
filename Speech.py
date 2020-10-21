import os
import random
import speech_recognition as sr
import pygame
from datetime import date
from datetime import datetime
from gtts import gTTS as tts
from Environment import *

#need to install
import wikipedia #pip install wikipedia
import pytz #pip install pytz

#Capture audio, input arg will be used to repeat question
def Capture(str):

    text_found = False

    rec = sr.Recognizer()
    
    while text_found == False:
        
        #Listen from microphone in 3 sec
        with sr.Microphone() as source:
            audio = rec.listen(source, phrase_time_limit=3) 
        
        #Recognize response from user 
        try:
            text = rec.recognize_google(audio, language="sv-SE")
            text_found = True
            return text
        
        #If no response, repeat question
        except:
            Speak(str)

#Speak to the user
def Speak(text):
    
    print(text) #Write output to console

    #Save audio file
    speech = tts(text=text, lang="sv")
    speech_file = "input.mp3"
    speech.save(speech_file)

    #Play audio file
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("input.mp3")
    pygame.mixer.music.play()
    
    #Wait for file to finish playing
    while pygame.mixer.music.get_busy():
         pygame.time.Clock().tick(1)
    
    #Remove file     
    os.remove(speech_file)
    
def Current_stockholm_time():
    #set timezone
    timezone = 'Europe/Stockholm'
    local_tz = pytz.timezone(timezone)
    
    #get current time
    now = datetime.datetime.now(pytz.utc)
    
    local_dt = now.replace(tzinfo=pytz.utc).astimezone(local_tz)
    now_local = local_tz.normalize(local_dt)
    
    return now_local.hour

def Greeting(currtime):
    #Greeting alternative
    if random.randint(0, 2) == 1:
        #First get name
        Speak('Hej,Vad heter du?')
        name = Capture('Ursäkta jag hörde inte, kan du säga ditt namn igen?')
        Speak('Hej, ' + str(name) + '.')
        
    else:
        if currtime < 12:
            Speak("Goddag")
        elif currtime < 18:
            Speak("God Eftermiddag")
        else:
            Speak("GodKväll")

def Goodbye(currtime):
    #Check time before 12
    if currtime < 12:
        lunch = 12 - currtime
        if lunch > 1 and lunch <= 3:
            Speak("Det är snart lunch, kämpa på")
        else:
            Speak("Ha en trevlig morgon")
    
    elif currtime == 12:
        Speak("Ha en trevlig lunch")
    
    #Check time after 12        
    elif currtime < 16:
        slut = 16 - currtime
        if slut > 1 and lunch <= 3:
            Speak("Det är snart slut för idag, kämpa på")
        else:
            Speak("Ha en trevlig eftermiddag")
    
    else:
        Speak("Ha en trevlig kväll")

#Conversation with the user
def Conversation():
    
    Greeting(Current_stockholm_time())
    
    #Ask how the user is feeling
    greeting_phrases=['Hur mår du?','Mår du bra idag?']
    choosen_phrase = random.choice(greeting_phrases)
    Speak(choosen_phrase)
    captured_text = Capture('Ursäkta jag hörde inte, mår du bra idag?').lower()
    
    if 'bra' in str(captured_text) or 'ja' in str(captured_text) or ' kanon' in str(captured_text) or 'fint' in str(captured_text):
            Speak("Det är bra att veta att du mår bra")
            
    elif 'dålig' in str(captured_text) or 'nej' in str(captured_text) or 'ont' in str(captured_text):
            Speak("Det var dålig att höra")
    
    #Then just keep listening & responding
    while 1:
        
        Speak('Vad kan jag hjälpa dig med?')
        captured_text = Capture('Ursäkta jag hörde inte, vad kan jag hjälpa dig med?').lower()
            

        if 'datum' in str(captured_text):
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            Speak(d1)
            
        elif 'hjälp' in str(captured_text):
            Speak('Det som jag kan hjälpa dig med: datum, temperatur, luftfuktighet, identifera en känd person/sak eller avsluta konvorsationen med att säga hejdå')

        elif 'hejdå' in str(captured_text):
            Goodbye(Current_stockholm_time())
            return
        
        elif 'temperatur' in str(captured_text):
            temp = Temperature()
            temp = str(temp)
            Speak('Temperaturen är ' + temp + ' grader celsius')
        
        elif 'luftfuktighet' in str(captured_text):
            humidity = Humidity()
            humidity = str(humidity)
            Speak('Luftfuktigheten är ' + humidity + ' %')
            
        elif 'vem är' in str(captured_text) or 'vad är'in str(captured_text): 
            Speak('Söker Wikipedia') 
            wikipedia.set_lang("sv")
            results = wikipedia.summary(str(captured_text), sentences = 1) 
            Speak("Enligt Wikipedia") 
            Speak(results) 
        
        else:
            Speak('Säg hjälp för att få reda på vad jag kan hjälpa med')

