# Some useful scripts for processing the MPII Movie Description dataset
Scripts I have used to process the MPII Movie Description dataset. I will keep the repository updated with new scripts I may happen to create.

## Getting Started
First of all, you will need to obtain the dataset. In order to do that, follow the instruction provided [here](https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/research/vision-and-language/mpii-movie-description-dataset/access-to-mpii-movie-description-dataset/).
Once you have access to the dataset, you may use `wgetParallelProtected.sh` to download the movie clips. This script was developed by the dataset creators and is available on the dataset page, I am just redistributing it here.

### utils.py
Code for extracting descriptions by movie id and calculating the total duration of the clips.

## scripts/downloadExtractAudio.sh
Downloads all clips contained in an input text file, extracts their audio track using ffmpeg, saves it as an uncompressed .wav file, and finally deletes the video file.
