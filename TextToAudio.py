from gtts import gTTS # pip install gtts
from playsound import playsound
# pip install playsound
audio = 'speech.mp3' 
language = 'en'
sp = gTTS(text = "I love you Jayasri and Brinda",
lang= language, slow=False)

sp.save(audio)
playsound (audio)