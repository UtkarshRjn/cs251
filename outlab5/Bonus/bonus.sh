#!/bin/bash

awk '
{
	if(NR==1){t=$1}
	if(NR%3==2){
		basei=int($1)
		baseo=int($2)
	}
	if(NR%3==0){
		x=int(1)
		input1=int(0)
		for(i=NF;i>=1;i--){
			var=$i
			if(var=="A")var=int(10)
			if(var=="B")var=int(11)
			if(var=="C")var=int(12)
			if(var=="D")var=int(13)
			if(var=="E")var=int(14)
			if(var=="F")var=int(15)
			input1 += (int(var))*x
			x=(x*basei);
		}
		x=int(1)
	}
	if(NR%3==1 && NR>1){
		y=int(1)
		input2=int(0)
		for(j=NF;j>=1;j--){
			var=$j
			if(var=="A")var=int(10)
			if(var=="B")var=int(11)
			if(var=="C")var=int(12)
			if(var=="D")var=int(13)
			if(var=="E")var=int(14)
			if(var=="F")var=int(15)
			input2 += (int(var))*y
			y=(y*basei);
		}
		y=int(1)
		result=input1+input2
		z=int(1)
		while(z/result<=1){z=z*baseo}
		while(z>1){
			z=z/baseo
			if(z==1){
				if(result/z<10){printf "%d",(result/z)}
					if(result/z>=10){
						var=result/z
						if(var==int(10))printf "A"
						if(var==int(11))printf "B"
						if(var==int(12))printf "C"
						if(var==int(13))printf "D"
						if(var==int(14))printf "E"
						if(var==int(15))printf "F"
					}
			}else{
				if(result/z<10){printf "%d ",(result/z)}
				if(result/z>=10){
					var=result/z
					if(var==int(10))printf "A "
					if(var==int(11))printf "B "
					if(var==int(12))printf "C "
					if(var==int(13))printf "D "
					if(var==int(14))printf "E "
					if(var==int(15))printf "F "
				}
			}
			
			result=result%z
			if(z==1)print ""
		}
		z=1
	}
}' OFS=" " bonus_sample_input.txt > bonus_output.txt