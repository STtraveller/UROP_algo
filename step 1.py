
#%%
import pandas as pd
import numpy as py


#%%
transcripts = pd.read_csv("transcript_metadata.csv",encoding = "ISO-8859-1")
audios = pd.read_csv("audio_metadata.csv")
transcripts_final = transcripts


#%%
transcripts.head()


#%%
audios.head()


#%%
audios.Ticker


#%%
audio_ticker_list = set(audios.Ticker)
len(audio_ticker_list)


#%%
# audios_test = audios.loc[(audios.Ticker == "CBB")]
audios_test = audios.loc[(audios.Ticker == "CBB") & (audios.Year == "2018")]
audios_test


#%%
# transcript_test = transcripts.loc[(transcripts.Symbol == "CBB")]
transcript_test = transcripts.loc[(transcripts.Symbol == "CBB") & (transcripts.Year == 2018)]
transcript_test


#%%
transcripts["Quarter"] = pd.to_datetime(transcripts.TextDateTime).dt.quarter


#%%
audios["Quarter"].head()


#%%
transcripts["Quarter"] = pd.to_datetime(transcripts["TextDateTime"]).dt.quarter


#%%
transcripts["Quarter"]=transcripts["Quarter"].fillna(0)
transcripts["Quarter"] = transcripts["Quarter"].astype(int)


#%%
date_list = []
for date in transcripts["TextDateTime"]:
    date_list.append(date[5:7]+ "/" + date[8:10] + "/" + date[0:4])
transcripts["Date"]= pd.DataFrame(date_list)


#%%
filename_list = []
for row in audios.itertuples(index=True, name='Pandas'):
    for transcript in transcripts.itertuples(index=True, name='Pandas'):
        if (transcript[3]==audio[1]) and (transcript[7]==audio[3]) and (transcript[15]==audio[2][1]) and (transcript[16]==audio[7]) and (transcript[1]==audio[4]):
            filename.append(audio[11])
            break
    filename.append("NaN")    
        
transcripts_final["the corresponding audio file name"] = pd.DataFrame(filename_list)
#%% [markdown]
# audio conversion
#%% [markdown]
# install ffmpeg, pydub before using
#%% [markdown]
# m4a -> mp3 increase file size a HELL LOT, be aware when using

#%%
from pydub import AudioSegment
import os

#%% [markdown]
# config the input output folders manually

#%%
path = os.getcwd()
audio_input_folder = "sample"
audio_output_folder = "audio_output"

#%% [markdown]
# single file conversion

#%%
sound = AudioSegment.from_file(path +"/" audio_input_folder + "/" + "1Q_2013_Pike_Electric_Corporation_Earnings_Conference_Call.m4a")
sound.export(path + "/" + audio_output_folder + "/" + "test.mp3", format="mp3", bitrate="128k")

#%% [markdown]
# batch conversion
#%% [markdown]
# BE AWARE OF THE LAGGGGGGGG

#%%
filelist = os.listdir(path + "/" + audio_input_folder)

#%% [markdown]
# file checking

#%%
for file in filelist:
    if len(file) <= 5:
        filelist.remove(file)
        print(file + " is wrong")
    elif file[-4:] != ".m4a":
        filelist.remove(file)
        print(file + " is wrong")


#%%
for file in filelist:
    sound = AudioSegment.from_file(path + "/" + audio_input_folder + "/" + file)
    mp3name = file[:-4] + ".mp3"
    sound.export(path + "/" + audio_output_folder + "/" + mp3name, format="mp3", bitrate="128k")


