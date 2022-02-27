# Modules requried for installation:
# pip install beautifulsoup4
# pip install google

# here webbrowser is used to open the tab of the google chrome
import webbrowser

# googlesearch is used to search the results and print it in the terminal
from googlesearch import search
# gtts is the google text to speech
from gtts import gTTS
# plays the sound 
from playsound import playsound
# converts the text to the speech and vice-versa
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
        # webbrowser will open the seach result in the new tab of the google chrome
        webbrowser.open_new_tab(j)
