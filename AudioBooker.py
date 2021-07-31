import pyttsx3
import easygui
file = easygui.fileopenbox()
while(file[-4:] != ".txt"):
	print("You have to choose a .txt file")
	file = easygui.fileopenbox()
f = open(file,"r")
sentence = f.readlines()
speaker = pyttsx3.init()
speaker.setProperty('rate', 100)
print("Converting, this may take a while")
path = ".mp3"
print(file)
sentence = sentence.replace("\n", "")
speaker.save_to_file(sentence, file+"toAudioBook"+path)
print("Output saved to the same directory as base file")
speaker.runAndWait()

