""" 
    Name: jarvis_speech_recognition2.py
    Author: Ygor Brito
    Created: 1/31/2022
    Purpose: Voice recognnition from google  
    """ 
#pip install SpeechRecognition
# install pyaudio

from sys import exit
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


engine = pyttsx3.init()
#pass text to say methof
engine.say('Danger Detected !!')
engine.say('Please give me instructions')
    
# run and Wait method processes the voice
engine.runAndWait()
class Jarvis:

    def __init__(self)  -> None:
    #Create SpeechRecognition recognizer object
     self.r = sr.Recognizer()
        
    def take_user_input(self):
        """recognizes user voice input usuing
        Speech Recognition module, converts it to text
        """
        #with your locar mic as the source
        with sr.Microphone() as source:
            print('Listening. . . .')
            self.r.pause_threshold = 1
            #Start listening for speech
            audio = self.r.listen(source)
            engine.say(audio)
        
            try:
                print('Recognizing. . .')
                
            # Capture the recognized word in a string variable
                self.query = self.r.recognize_google(audio, language='en-in')
                
                print(self.query)       #Print thw speech
                engine.say(self.query) # Jarvis repeat the words
                engine.runAndWait()
                
                engine.say('There is anyhting else I can do Mr Brito ?')
                engine.runAndWait()
        
                   
            except sr.UnknownValueError:
                print("Googlr Speech Recognition could not understant audio")
            
            except sr.RequestError as e:
                #If there was an error communicasting with Google Speech
                print(f"Google Speech did not respond:  {e}")
                
            
    
            
    def voice_commands(self):
        if self.query == "quit":
            engine.say('Thanks for your instructions')
            engine.runAndWait()
            print("Goodbye!")
            
            exit()
        
#Create a jarvis program ovject
jarvis = Jarvis()
while True:
     jarvis.take_user_input()
     jarvis.voice_commands()      
     
                

