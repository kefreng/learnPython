from gtts import gTTS

from playsound import playsound

audio = 'speech.mp3'
language = 'es'
sp = gTTS(text="Por favor, utilice su mascarilla.",
          lang=language,
          slow=False)

sp.save(audio)
playsound(audio)