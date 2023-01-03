import numpy as np
import os
import pandas as pd


def load_participant(nbparticipants, questions_type, group_id):

    # create panda dataframe to store audio features
    df = pd.DataFrame(columns = ['Participant_id', 'Group', 'Question', 'Speech rate', 'Articulation rate', 'Pitch frequency', 'WER of the VSR model'])

    # Retrieve features of interest, put them all in the panda dataframe
    for participant_id in range(nbparticipants):
    
        for i, g in enumerate(group_id):

            for q, question in enumerate(questions_type):
                #print((participant_id*200)+(i*100)+(q*20)+6)

                tmp = features[(participant_id*200)+(i*100)+(q*20)+6][20:28]
                tmp = tmp.replace('\x00','')
                speech_rate = float(tmp)

                tmp = features[(participant_id*200)+(i*100)+(q*20)+7][20:28]
                tmp = tmp.replace('\x00','')
                articulation_rate = float(tmp)
                
                tmp = features[(participant_id*200)+(i*100)+(q*20)+11][20:28]
                tmp = tmp.replace('\x00','')
                pitch_freq = float(tmp)

                df = df.append({'Participant_id' : participant_id, 'Group' : g, 'Question' : question,
                                'Speech rate' : speech_rate, 'Articulation rate' : articulation_rate, 
                                'Pitch frequency' : pitch_freq, 'WER of the VSR model' : 0.0}, 
                                ignore_index = True)

    return df


def extract_mean(df):

    df_means = df.groupby(['Participant_id', 'Group']).mean()
    return df_means


def extract_mean_questions(df):

    df_means = df.groupby(['Group', 'Question']).mean() #.describe()
    print(df_means)
    return df_means



if __name__ == '__main__':

    # Upload list of questions for each group
    questions_type = ['presentation', 'hollidays', 'sports', 'music', 'cooking']
    group_id = ["human", "robot"]
    nbparticipants = 10  # number of participants

    # file with all the audio features
    features_file = "audio_features.txt"
    # Link to retrieve the feature file
    current_path = current_path = os.path.dirname(os.path.realpath(__file__))

    # open features file and load content
    # ATTENTION: DO NOT FORGET TO CHANGE THE TXT FILE ENCODING TO ANSI (easier to process the line numbers)
    file = open(features_file)
    features = file.readlines()

    # Retrieve features of interest, put them all in a panda Dataframe
    data = load_participant(nbparticipants, questions_type, group_id)
    print(data)
    #save the panda dataframe to a csv file
    data.to_csv('audio_features.csv')

    data_means_by_part_by_group = extract_mean(data)
    data_means_by_part_by_group.to_csv('mean_audio_features.csv')

    data_means_by_questions_by_group = extract_mean_questions(data)
    data_means_by_questions_by_group.to_csv('stat_audio_features_per_questions.csv')




    