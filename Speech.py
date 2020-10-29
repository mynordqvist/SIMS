import os
import random
import speech_recognition as sr
import pygame
from datetime import date
from datetime import datetime
from gtts import gTTS as tts
from Environment import *
import wikipedia 
import pytz
import globals
import time

#Capture audio, input arg will be used to repeat question
def Capture(str):

    text_found = False
    rec = sr.Recognizer()
    
    while text_found == False:
        
        #Listen from microphone in 3 sec
        with sr.Microphone() as source:
            audio = rec.listen(source, phrase_time_limit=3)
        
        #Try to recognize response from user, otherwise print error and try again, max 3 times   
        try:
            text = rec.recognize_google(audio, language="sv-SE")
            text_found = True
            return text
        
        #If it detects noise that cannot be interpreted
        except sr.UnknownValueError:
            print("value error")
            Speak(str)
            globals.count = globals.count + 1
            if globals.count == 3:
                globals.count = 0
                return 'Hejdå'
        
        #If no response, repeat question, max 3 times
        except:
            Speak(str)
            globals.count = globals.count + 1
            if globals.count == 3:
                globals.count = 0
                return 'Hejdå'
            

#Speak to the user
def Speak(text):
    
    print(text) #Write output to console
    
    #Try to save string to mp3 and play, otherwise print error and try again    
    while True:

        try:
            #Save audio file
            speech = tts(text=text, lang="sv", lang_check=False)   
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
            return
            
        except Exception as e:
            e = str(e)
            print("error: " + e)
            
    
def Current_hour():
    #Set timezone
    timezone = 'Europe/Stockholm'
    local_tz = pytz.timezone(timezone)
    
    #Get current time
    now = datetime.now(pytz.utc)
    
    local_dt = now.replace(tzinfo=pytz.utc).astimezone(local_tz)
    now_local = local_tz.normalize(local_dt)
    
    return now_local.hour

def Current_time():
    #Set timezone
    timezone = 'Europe/Stockholm'
    local_tz = pytz.timezone(timezone)
    
    #Get current time
    now = datetime.now(local_tz)
    
    #Get hour and minutes
    time = now.strftime("%H %M")
    
    return time

def Greeting(currtime):
    #Greeting alternative
    if random.randint(0, 2) == 1:
        #Get name
        Speak('Hej,Vad heter du?')
        name = Capture('Ursäkta jag hörde inte, kan du säga ditt namn igen?')
        #End conversation
        if 'Hejdå' in str(name):
            return 'exit'
        Speak('Hej, ' + str(name) + '.')
        
    else:
        if currtime < 10:
            Speak("God morgon")
        elif currtime < 13:
            Speak("God dag")
        elif currtime < 18:
            Speak("God Eftermiddag")
        else:
            Speak("GodKväll")

def Goodbye(currtime):
    
    #Randomly end with corona phrases
    corona_phrases=['Och kom ihåg att hålla avstånd','Och glöm inte bort att tvätta händerna', 'Och kom ihåg att hosta och nys i armvecket', ' ']
    choosen_phrase = random.choice(corona_phrases)
    
    #Check time before 12
    if currtime < 12:
        lunch = 12 - currtime
        if lunch > 1 and lunch <= 3:
            Speak("Det är snart lunch, kämpa på " + choosen_phrase)
        else:
            Speak("Ha en trevlig dag " + choosen_phrase)
    
    elif currtime == 12:
        Speak("Ha en trevlig lunch " + choosen_phrase)
    
    #Check time after 12        
    elif currtime < 16:
        slut = 16 - currtime
        lunch = 12 - currtime
        if slut > 1 and lunch <= 3:
            Speak("Det är snart slut för idag, kämpa på " + choosen_phrase)
        else:
            Speak("Ha en trevlig eftermiddag " + choosen_phrase)
    
    else:
        Speak("Ha en trevlig kväll " + choosen_phrase)

#Conversation with the user
def Conversation():
    
    #End conversation
    exitNow = Greeting(Current_hour())
    if 'exit' in str(exitNow):
        Goodbye(Current_hour())
        return
    
    #Ask how the user is feeling
    greeting_phrases=['Hur mår du?','Mår du bra idag?', 'Hur är läget?', 'Är allt bra med dig?', 'Hur är det med dig?' ]
    choosen_phrase = random.choice(greeting_phrases)
    Speak(choosen_phrase)
    globals.count = 0
    captured_text = Capture('Ursäkta jag hörde inte, mår du bra idag?')
    captured_text = captured_text.lower()
    if 'hejdå' in str(captured_text): #exit conversation
        Goodbye(Current_hour())
        return
    
    #If the user is feeling good
    if 'bra' in str(captured_text) or 'ja' in str(captured_text) or ' kanon' in str(captured_text) or 'fint' in str(captured_text):
        response_phrases=['Det är skönt att höra att du mår bra','Vad roligt att höra', 'Härligt att du mår bra', 'Toppen', 'Underbart att höra' ]
        choosen_phrase = random.choice(response_phrases)
        Speak(choosen_phrase)
    
    #If the user is feeling bad
    elif 'dåligt' in str(captured_text) or 'nej' in str(captured_text) or 'ont' in str(captured_text):
        response_phrases=['Det var tråkigt, men jag vet att du kommer ta dig igenom det','Oavsett tycker jag att du ska vara stolt över dig själv', 'Jag vill att du ska tro på dig själv', 'Bara så du vet, det bästa har ännu inte kommit', 'Så länge du gör ditt bästa så kommer det gå galant' ]
        choosen_phrase = random.choice(response_phrases)
        Speak(choosen_phrase)
    
    #Listening & responding
    while 1:
        Speak('Vad kan jag hjälpa dig med?')
        globals.count = 0
        captured_text = Capture('Säg hjälp för att få reda på vad jag kan hjälpa dig med').lower()
            

        if 'datum' in str(captured_text) or 'dag' in str(captured_text):
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            Speak('Idag är det den ' + d1)
            
        elif 'hjälp' in str(captured_text):
            Speak('Jag kan hjälpa dig med datum, klockan, temperatur, luftfuktighet, identifera en känd person/sak eller avsluta konversationen med att säga hejdå')

        elif 'hejdå' in str(captured_text):
            Goodbye(Current_hour())
            return
        
        elif 'klockan' in str(captured_text) or 'tid' in str(captured_text):
            time = Current_time()
            time = str(time)
            Speak('Klockan är ' + time)
        
        elif 'temperatur' in str(captured_text) or 'varmt' in str(captured_text) or 'grader' in str(captured_text):
            temp = Temperature()
            temp = str(temp)
            Speak('Temperaturen är ' + temp + ' grader celsius')
        
        elif 'luftfuktighet' in str(captured_text):
            humidity = Humidity()
            humidity = str(humidity)
            Speak('Luftfuktigheten är ' + humidity + ' %')
            
        elif 'luft' in str(captured_text) or 'syre' in str(captured_text) or 'syrenivå' in str(captured_text) or 'koldioxid' in str(captured_text):
            air = Co2()
            Speak('Luftkvaliten är ' + air)
            
        elif 'vem är' in str(captured_text) or 'vad är'in str(captured_text): 
            
            #Try to search on Wikipedia, otherwise say "no result"
            try:
                Speak('Jag söker på Wikipedia') 
                wikipedia.set_lang("sv")
                results = wikipedia.summary(str(captured_text), sentences = 1)
                Speak("Enligt Wikipedia") 
                Speak(results)
            except:
                Speak("Jag hittade inget om " + captured_text)

#Call Doris
def Hey():
    
    while True:
        time.sleep(0.1)
        while globals.hey_found == False:

            rec = sr.Recognizer()
                
            #Listen from microphone in 3 sec
            with sr.Microphone() as source:
                audio = rec.listen(source, phrase_time_limit=3)
                
            #Try to get response from user, otherwise sleep short time
            try:
                text = rec.recognize_google(audio, language="sv-SE")
                text = text.lower()
                print ('text: ' + text)
                
                if 'hej doris' in str(text) or 'hej louise' in str(text) or 'hej boris' in str(text) or 'hej google' in str(text):
                    globals.hey_found = True
            except:
                time.sleep(0.01)
                
        
            
            

