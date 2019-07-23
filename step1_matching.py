import pandas as pd
import numpy as py

transcripts = pd.read_csv("transcript_metadata.csv", encoding = "ISO-8859-1")
audios = pd.read_csv("audio_metadata.csv")
transcripts_final = transcripts

transcripts["TextDateTime"] = transcripts["TextDateTime"].astype(str)
transcripts["Year"] = transcripts["Year"].astype(str)
transcripts["Quarter"] = pd.to_datetime(transcripts["TextDateTime"]).dt.quarter
transcripts["Quarter"] = transcripts["Quarter"].fillna(0)
transcripts["Quarter"] = transcripts["Quarter"].astype(int)

dates_list = []
audios["Date"] = audios["Date"].astype(str)
for date in audios["Date"]:
    date_list = date.split("/")
    if len(date_list[0]) == 1:
        date_list[0] = "0" + date_list[0]
    if len(date_list[1]) == 1:
        date_list[1] = "0" + date_list[1]
    dates_list.append("/".join(date_list))
audios["Date"] = pd.DataFrame(dates_list)

date_list = []
for date in transcripts.TextDateTime:
    try:
        temp = date[5:7]+ "/" + date[8:10] + "/" + date[0:4]
    except BaseException:
        date_list.append(0)
    else:
        date_list.append(temp)
transcripts["Date"] = pd.DataFrame(date_list)

filename_list = []
for transcript in transcripts.itertuples(index=True, name='Pandas'):
    flag = False
    for audio in audios.loc[(audios["Ticker"] == transcript[3]) & (audios["Date"] == transcript[16])].itertuples(index=True, name='Pandas'):
        filename_list.append(audio[11])
        flag = True
        break
    if not flag:
        filename_list.append("NaN")
    if transcript[0] % 10000 == 0:
        print(transcript[0])
transcripts_final["the corresponding audio file name"] = pd.DataFrame(filename_list)

transcripts_final.to_csv("final.csv", index=False)
