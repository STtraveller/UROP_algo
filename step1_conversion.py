from pydub import AudioSegment
import os


path = os.getcwd()
audio_input_folder = "audio_sample"
audio_output_folder = "audio_output"

filelist = os.listdir(path + "/" + audio_input_folder

for file in filelist:
    if len(file) <= 5:
        filelist.remove(file)
        print(file + " is wrong")
    elif file[-4:] != ".m4a":
        filelist.remove(file)
        print(file + " is wrong")

for file in filelist:
    sound = AudioSegment.from_file(path + "/" + audio_input_folder + "/" + file)
    mp3name = file[:-4] + ".mp3"
    sound.export(path + "/" + audio_output_folder + "/" + mp3name, format="mp3", bitrate="128k")
