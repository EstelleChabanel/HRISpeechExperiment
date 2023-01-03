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


def extract_participant(participant_id):
    
    video_path_ = os.path.join(video_path, 'p' + str(participant_id))

    for g in group_id:
        if (g == "human"):
            filename = "q"
        else:
            filename = "rq"

        for i in questions_type:
            filename_ = video_path_ + filename + i
            print("Participant", participant_id, ", group: ", g, ", question: ", i, "\n")

            #os.chdir(video_path_)
            print(filename_)
            extract_audio(filename_ + ".mp4",   #".avi"
                            filename_ + ".wav")  
            print("\n")



if __name__ == '__main__':

    # Upload list of questions for each group
    #questions_type = ['presentation', 'hollidays', 'sports', 'music', 'cooking']
    questions_type = ['1', '2', '3', '4', '5']
    group_id = ["human", "robot"]

    # To retrieve the videos
    nbparticipants = 10  # number of participants
    video_path = r'C:\Users\eecha\OneDrive\Documents\EPFL-Master\Semestre3\ProjetSemestre\FinalTestExperience\Recordings'
    #video_path = os.path.dirname('\Recordings')
    #video_path = os.path.dirname(os.path.realpath('__file__'))

    for i in range(nbparticipants):
        extract_participant(i+1)
        os.chdir(video_path)