from typing import Text
from gtts import gTTS 
#pip install gtts
from playsound import playsound
#pip install playsound

audio = 'speech.mp3'
languaje = 'es'
sp = gTTS(text = " Prueba de voz", lang = languaje, slow = False)

sp.save(audio)
playsound(audio)
