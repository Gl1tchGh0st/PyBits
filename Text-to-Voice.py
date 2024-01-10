# Note ---- The spelling must be correct or will give an error

from gtts import gTTS
import os

speaktext = str(input("Enter what you wish to say here: "))
print("Make sure to spell it correctly or the file won't run. ")
language  = "en"
myobj = gTTS(text = speaktext, lang = language, slow = False)
myobj.save("myText.mp3")
os.system("mpg321 myText.mp3")
