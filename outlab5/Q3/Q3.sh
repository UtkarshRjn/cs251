#!/bin/bash

temp_file=$(mktemp)
temp_file2=$(mktemp)
temp_file3=$(mktemp)

awk -F '[\| | : | -]' -v N="$N" '
{
	if($1==1){
		for(i=2; i<=NF; i++){
			count[$i]++
		}
	}
}
END{
	for(i in count){
		printf "%d %d \n",i , count[i]
	}
}' "sample.txt" > "temp_file"

awk '{print $1, $2| "sort -k 2,2nr -k 1,1n "} ' "temp_file" > "temp_file2"

awk '{print | "sort"}' word_token_mapping.txt > sorted.txt

awk -F '[\| | : | -]' '
{if(NR==FNR){j=0+$2;word[j]=$1;}
if(NR!=FNR){k=0+$1; print word[k],$2 | "sort -k 2,2nr -k 1,1"}
}
' "sorted.txt" "temp_file2" > "temp_file3"

awk -v N=$1 '{if(NR<=N){print $1}}' "temp_file3" > "spam.txt"

rm -rf "temp_file"
rm -rf "temp_file2"
rm -rf "temp_file3"

tempfile=$(mktemp)
tempfile2=$(mktemp)
tempfile3=$(mktemp)

awk -F '[\| | : | -]' -v N="$N" '
{
	if($1==0){
		for(i=2; i<=NF; i++){
			count[$i]++
		}
	}
}
END{
	for(i in count){
		printf "%d %d \n",i , count[i]
	}
}' "sample.txt" > "tempfile"

awk '{print $1, $2| "sort -k 2,2nr -k 1,1n "} ' "tempfile" > "tempfile2"

awk -F '[\| | : | -]' '
{if(NR==FNR){j=0+$2;word[j]=$1;}
if(NR!=FNR){k=0+$1; print word[k],$2 | "sort -k 2,2nr -k 1,1"}
}
' "sorted.txt" "tempfile2" > "tempfile3"

awk -v N=$1 '{if(NR<=N){print $1}}' "tempfile3" > "ham.txt"

rm -rf "sorted.txt"
rm -rf "tempfile"
rm -rf "tempfile2"
rm -rf "tempfile3"