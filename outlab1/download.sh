#!/bin/bash

if [ $# -eq 2 ]
then
	wget -r -nH --cut-dirs=$2 --no-parent --reject="index.html*" $1
	if [ $(basename $1) != "mock_grading" ]
	then
		mv $(basename $1) mock_grading
	fi
else
	echo "Usage: bash download.sh <link to directory> <cut-dirs argument>"
	test $# -eq 2 
	echo $?
fi