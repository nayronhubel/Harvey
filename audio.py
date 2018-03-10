import wget
import speech_recognition as sr
import os
import subprocess

def Track(url):
     rec = sr.Recognizer()
     filename = wget.download(url)
     command = "cd C:\\ffmpeg\\bin\\ && ffmpeg -i \""+os.getcwd()+"\\" +filename+"\" -ab 160k -ac 2 -ar 44100 -vn \""+os.getcwd()+"\\"+filename+".wav\""
     subprocess.call(command, shell=True)
     with sr.AudioFile(filename+".wav") as source:
        audio = rec.record(source)
     response_sent_nontext = rec.recognize_google(audio,language="pt")
     return response_sent_nontext