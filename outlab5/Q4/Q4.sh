#!/bin/bash

awk -F['\t',] -v arg1=$2 -v arg2=$3 '
function timesum(t,s){
    gsub(/[:/]/," ", t)
    gsub(/[:/]/," ", s)
    split(t,a1," ")
    split(s,a2," ")
    sec = a1[4]*3600+a1[5]*60+a1[6]
    sec +=  a2[4]*3600+a2[5]*60+a2[6]
    h=int(sec/3600)
    m=int((sec-3600*h)/60)
    s=sec-3600*h-60*m 
    return strftime("%d/%m/%Y %H:%M:%S",mktime("2020 8 19 "h" "m" "s""));
}
function timediff(t, s){
    gsub(/[:/]/," ", t)
    gsub(/[:/]/," ", s)
    d1 = mktime(t)
    d2 = mktime(s)
    return strftime("%d/%m/%Y %H:%M:%S",d1-d2);
}
NR!=1{
	if($2 == "Joined"){
		if($4 < " "arg1){
			a[$1] = timesum(a[$1], timediff($3" "arg2,$3" "arg1));
		}
		else{
			a[$1] = timesum(a[$1], timediff($3" "arg2 ,$3" "$4));
		}
	}else{
		if($4 < " "arg2){
			# print $4
			a[$1] = timediff(a[$1], timediff($3" "arg2 ,$3" "$4));
		}
	}
	if(f != $1 && NR>2){
		split(a[f],b," ")
		print f"\t"b[2] | "sort";
	}
	f=$1;
}
END{
	split(a[f],b," ")
	print f"\t"b[2] | "sort";
}
' $1 > output.txt