#!/bin/bash

touch distribution.txt marksheet.csv

cd organised

for roll in $( cut -d "" -f 2 '../mock_grading/roll_list' )
do
	cd $roll
	mkdir student_outputs
	
	let marks=0
	for input in $(basename -a ../../mock_grading/inputs/*.in)
	do
		g++ -o executable $roll.cpp 2>/dev/null 
		timeout 5s ./executable < ../../mock_grading/inputs/$input > student_outputs/${input%.in}.out 2>/dev/null |:
	
		if diff student_outputs/${input%.in}.out ../../mock_grading/outputs/${input%.in}.out > /dev/null
		then
			(( marks++ ))
		fi
	done
	
	echo $marks >> ../../distribution.txt
	echo $roll,$marks >> ../../marksheet.csv
	
	cd ..
done
cd ..

sort -rno distribution.txt distribution.txt
sort -o marksheet.csv marksheet.csv