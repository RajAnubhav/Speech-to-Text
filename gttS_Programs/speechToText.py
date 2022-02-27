# first of all import the speech_recognition module as sr
# if this module is not present then, type in terminal pip install SpeechRecognition

#****************   REGARDING THE ERROR   ******************* 
# so, here we're going to get an error of pyaudio. How to resolve it?
# goto unofficial python binaries and search for PyAudio
# download and install it 
# then, again type in terminal pip install pyaudio

#<<<<<------------  CONGRATULATIONS THE ERROR IS RESOLVED    ---------------->>>>>>

import speech_recognition as sr
#<<<<-------------   Recognizer is used for recognizing the audio from the mic   ---------------------------->>>>>
r = sr.Recognizer()

#<<<<-------  Now open the sr.Microphone as the source    ------------------>>>>>
with sr.Microphone() as source:
    print("Speak Anything...")
    
    #<<<<<-----------------   store the audio input from the user to the variable named audio  ------------>>>>
    audio=r.listen(source)
    
    #<<<<<-----------------   use the reconize_google to convert the audio input into the text   ----------->>>>>
    text=r.recognize_google(audio)

    #<<<<<--------------    Print the input in the output   ------------------>>>>>>>>>>>
    print("You said : {}".format(text))