# installation:
# pip install beautifulsoup4
# pip install google

import webbrowser
from googlesearch import search
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

# asking input from the user
myText = "How can I help you ?"
audio = gTTS(text=myText, lang="en", slow=False)
audio.save("myAudio.mp3")
playsound("myAudio.mp3")

# to get audio input from the user
r = sr.Recognizer()
print("Please say something...")
with sr.Microphone() as source:
    userAudio=r.listen(source)
    userText=r.recognize_google(userAudio)
    print("You said: {}".format(userText))
    # now do google search
    for j in search(userText, tld="co.in", num=1, stop=1):
        print(j)
        webbrowser.open_new_tab(j)