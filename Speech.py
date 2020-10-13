import os
import random
import speech_recognition as sr
import pygame
from datetime import date
from datetime import datetime
from gtts import gTTS as tts

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

#Conversation with the user
def Conversation():
    
    #First get name
    Speak('Hej,Vad heter du?')
    name = Capture('Ursäkta jag hörde inte, kan du säga ditt namn igen?')
    Speak('Hej, ' + str(name) + '.')

    #Ask how the user is feeling
    greeting_phrases=['Hur mår du?','Mår du bra idag?']
    choosen_phrase = random.choice(greeting_phrases)
    Speak(choosen_phrase+' '+name)
    captured_text = Capture('Ursäkta jag hörde inte, mår du bra idag?').lower()
    
    #Then just keep listening & responding
    while 1:
        
        Speak('Vad kan jag hjälpa dig med?')
        captured_text = Capture('Ursäkta jag hörde inte, vad kan jag hjälpa dig med?').lower()
            

        if 'datum' in str(captured_text):
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            Speak(d1)
            
        elif 'hjälp' in str(captured_text):
            Speak('Tillgängliga funktioner: hälsning, datum, hejdå och hjälp')

        elif 'hejdå' in str(captured_text):
            Speak('Okej, hejdå ' + name + ', ha en trevlig dag.')
            #break
            return
        
        else:
            Speak('Säg hjälp för att få tillgängliga funktioner')
