import speech_recognition as sr

r=sr.Recognizer()

a=sr.AudioFile('res.wav')
with a as source :
	audio=r.record(source)

text=r.recognize_google(audio)


file1=open(r"C:\Users\91974\Desktop\python\speech.txt","a")
file1.writelines(text)
file1.close()