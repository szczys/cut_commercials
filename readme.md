# Cut commercials

Script to generate FFMPEG commands that cut commercials out of an over-the-air recording

* Set the input file as `infile` variable
* Manually find the timestamps for start and stop of each episode and enter them in `segments` array
* Run ./commercials.py

Script will output a oneliner that creates one file for each segment, and concatenates them into `output.mp4`
