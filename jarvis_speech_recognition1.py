""" 
    Name: jarvis_speech_recognition.py
    Author: Ygor Brito
    Created: 1/31/2022
    Purpose: Voice recognnition from google  
    """ 

import speech_recognition as sr 

#Create SpeechRecognition recognizer object
r = sr.Recognizer()

#With your local microphone as the source
with sr.Microphone() as source:
    print('Listening . . . .')
    audio = r.listen(source)
    
    try:
        print('Recognizing . . .')
        #Capture the recognized word in a variable
        print(f" You may have said: {r.recognize_google(audio)}")
                  
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        
    except sr.RequestError as e:
        # If there was an erro communicating with Google Speech
        print(f"Google Speech did not respond: {e}")