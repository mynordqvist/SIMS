import os
from datetime import date
from datetime import datetime
import random

import speech_recognition as sr
import pyttsx3

from playsound import playsound
from gtts import gTTS as tts


def capture():
    """Capture audio"""

    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print('I\'M LISTENING...')
        audio = rec.listen(source, phrase_time_limit=5)

    try:
        text = rec.recognize_google(audio, language="sv-SE")
        return text
    except rec.RequestError:
        engine = pyttsx3.init()
        engine.say('API unavailable')
        #wait for it to say everything
        engine.runAndWait()  
        return 0
    
    except:
        speak('Ursäkta jag fattar inte, säg hjälp för att få funktioner')
        return 0
    
def process_text(name, input):
    """Process what is said"""

    speak(name + ', du säger: "' + input + '".')
    return

def speak(text):
    """Say something"""

    # Write output to console
    print(text)

    # Save audio file
    speech = tts(text=text, lang='sv')
    speech_file = 'input.mp3'
    speech.save(speech_file)

    # Play audio file
    playsound("input.mp3")
    os.remove(speech_file)
    

if __name__ == "__main__":

    
    # First get name
    speak('Hej,Vad heter du?')
    name = capture()
    speak('Hej, ' + name + '.')

    # Then just keep listening & responding
    greeting_phrases=['Hur mår du?','Mår du bra idag']
    choosen_phrase = random.choice(greeting_phrases)
    speak(choosen_phrase+' '+name)
    #captured_text = capture().lower()
    
    while 1:
        
        speak('vad vill du?')
        captured_text = capture().lower()
            
        if 'tid' in str(captured_text):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            speak(current_time)

        if 'datum' in str(captured_text):
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            speak(d1)
            
        if 'hjälp' in str(captured_text):
            speak('tillgängliga funktioner: hälsning, tid, datum, hejdå och hjälp')

        if 'hejdå' in str(captured_text):
            speak('Okej, hejdå ' + name + ', ha en trevlig dag.')
            break

        # Process captured text
        process_text(name, captured_text)
