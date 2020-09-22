import speech_recognition as sr
import pyttsx3
from googletrans import Translator
#import time

#might need to use class
def recognize_speech_from_mic_to_text(recognizer, microphone):
    #check if correct instances
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
        
    #recognize_speech
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    #create response
    response = {
    "success": True,
    "error": None,
    "transcription": None
    }
    
    #add values to response
    try:
        response["transcription"] = recognizer.recognize_google(audio, language="sv-SE")
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
        
    print(response["transcription"])
    
    return response

def translate(text,lang):
    #need to figure out dest language
    #create instance
    translator = Translator()
    #translate to swedish
    translated = translator.translate(text, dest='sv')
    print(translated.text)
    
    return translated.text

def tts(text):
    #need work with response/response in diff. langauge 
    #text_to_speech
    engine = pyttsx3.init()
    
    engine.say(text)
    
    #wait for it to say everything
    engine.runAndWait()  
        
    return 0

if __name__ == "__main__":  
    #create instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    #use recognize_speech_from_mic_to_text
    text =recognize_speech_from_mic_to_text(recognizer, microphone)
    tts(text["transcription"])
    