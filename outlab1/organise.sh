#!/bin/bash

mkdir organised
cd organised

for roll in $( cut -d "" -f 2 '../mock_grading/roll_list' )
do
	mkdir $roll
	cd $roll
	ln -sF "../../mock_grading/submissions/$( cd ../../;basename -a $(find . -type f -path "../../mock_grading/submissions/$roll*" ))" $(cd ../../;basename -a $(find . -type f -path "../../mock_grading/submissions/$roll*" ))
	cd ..
done