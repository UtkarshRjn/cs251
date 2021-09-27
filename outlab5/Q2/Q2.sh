#!/bin/bash

awk '
BEGIN {
	j=1;
}
{
	for(i=1;i<=NF;i++){
		if(!a[$i]){
			a[$i]=j;
			j++;
		}
		if(i<NF) printf a[$i]-1" ";
		else printf a[$i]-1;
	}
	print "";
}
' sample.txt > output.txt