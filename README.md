# Speech characteristics when interacting with lip-reading social robot

This repository contains the code and report for an experiment conducted at the CHILI laboratory. The experiment explores humans' speech characteristics when interacting with lip-reading social robots.

A short description of the experiment along with the results can be found in the `Summary` pdf file, more detailed descriptions and conclusions are presented in the `Report`.


## How to use the code
Original data used for the presentation of the results are not given in the repository since it includes participants images and recordings.
The experiment collected video datas that weere analzyed using the given codes in the following order:
* `1.audio_extraction.py` for extraction of the audio data.
* `2.audiofeatures_extraction.py` for collection of the audio features from audio data (speech rate, articulation rate, mean pitch frequency). The features are gathered in external `.txt` file (one should change its encodings to ANSI for usability issue) by running the following command in the terminal:
```
run python 2.audiofeatures_extraction.py >> audio_features.txt
```
* `3.audio_analysis.py` to gather all audio features along with experiment's information in pandas dataframes saved in `.csv` files
* `4.audio_analysis.ipynb` present some visual analysis of the extracted features

The code for evaluating the performance of the Visual Speech Recognition robot can be found in this [repository](https://github.com/CHILIpReading)
