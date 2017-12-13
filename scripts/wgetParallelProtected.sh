#!/bin/bash


EXPECTED_ARGS=3
E_BADARGS=65

if [ $# -lt $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` <filesToDownload> <username> <password> [parallelDownloads=8]"
  exit $E_BADARGS
fi
filesToDownload=$1
username=$2
password=$3
parallelDownloads=$4

if [ $# -lt 4 ]
then
	parallelDownloads=8
fi

cat $filesToDownload | xargs -n 1 -P $parallelDownloads wget --cut-dirs=2 -q --user=$username --password=$password
