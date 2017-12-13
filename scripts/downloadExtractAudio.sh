#!/bin/bash

EXPECTED_ARGS=1
E_BADARGS=65

if [ $# -lt $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` <filesToDownload> <username> <password>"
  exit $E_BADARGS
fi
filesToDownload=$1
username=$2
password=$3


for p in $(cat $filesToDownload)
do
  echo "Downloading $p"
  clp=$(python3 get_name.py 0 $p)
  wget -crnH -q $clp --cut-dirs=2 -q --user=$username --password=$password --auth-no-challenge
  f=$(python3 get_name.py 1 $p)
  sleep 1
  echo "Converting $f"
  ffmpeg -nostats -loglevel 0 -i "$f" -vn -acodec pcm_s16le -ar 44100 -ac 1 "$f.wav"
  echo "Converted"
  sleep 1
  rm $f
  echo "Removed"
done
