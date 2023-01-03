import numpy as np
import random
import json
import cv2
import os
import moviepy.editor as mp
from pydub import AudioSegment



def extract_audio(video_filename, audio_filename):

    #extract audio from the video
    my_clip = mp.VideoFileClip(filename=video_filename)
    #save the audio in a separate wave file
    my_clip.audio.write_audiofile(audio_filename, fps=44000, nbytes=2, buffersize=2000, codec="pcm_s16le")
    my_clip.close()


def extract_speech_properties(audio_filename, audio_path):
    # From each audio, extract all audio information, will be savec in a unique file
    #audio_segment = AudioSegment.from_file(audio_filename)

    # Save audio info in a separate dict
    #audio_dict = {"channel": audio_segment.channels,
     #           "sample width": audio_segment.sample_width,
      #          "frame rate (sample rate)": audio_segment.frame_rate,
        #        "frame width": audio_segment.frame_width,
       #         "length (ms)": len(audio_segment),
         #       "frame count": audio_segment.frame_count(),
          #      "intensity": audio_segment.dBFS
           #     }

    mysp=__import__("my-voice-analysis")
    mysp.mysptotal(audio_filename, audio_path)


def extract_participant(participant_id):
    
    filename = "p" + str(participant_id)

    for g in group_id:
        if (g == "human"):
            filename_end = "q"
        else:
            filename_end = "rq"

        for i in questions_type:
            filename_ = filename + filename_end + i
            print("Participant", participant_id, ", group: ", g, ", question: ", i, "\n")
            #print(filename_)
            #print(audio_path)
            extract_speech_properties(filename_, audio_path)
            print("\n")



if __name__ == '__main__':

    # Upload list of questions for each group
    #questions_type = ['presentation', 'hollidays', 'sports', 'music', 'cooking']
    questions_type = ['1', '2', '3', '4', '5']
    group_id = ["human", "robot"]

    # To retrieve the videos
    nbparticipants = 10  # number of participants

    current_path = os.getcwd()
    audio_path = os.path.join(current_path, "Recordings")
    os.chdir(audio_path)

    for i in range(nbparticipants):
        extract_participant(i+1)
        os.chdir(audio_path)



# ============================================================================================== #


### TO RUN:
### >>> python 2.audiofeatures_extraction.py >> audio_features.txt
### once the file created don't forget to change its encoding to ANSIS !