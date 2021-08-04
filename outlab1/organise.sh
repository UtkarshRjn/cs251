#!/bin/bash

mkdir organised
cd organised

for roll in $( cut -d "" -f 2 '../mock_grading/roll_list' )
do
	mkdir $roll
	cd $roll
	for file in $( cd ../../;basename -a $(find . -type f -name "$roll*"))
	do
		ln -sF ../../mock_grading/submissions/$file $file
	done
	cd ..
done