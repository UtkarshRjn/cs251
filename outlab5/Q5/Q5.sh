#!/bin/bash

# dos2unix sample.txt
awk -F'[<>]' '
BEGIN{
	j = 0;
}
FNR==NR{gsub(/[\r\n]/,"", $0);a[j]=$0;j++;next}
{
	for(i=0;i<NR-FNR;i++){
		if($0 ~ a[i]"</div>")
			arr[i] = $27;
	}
}
END{
	for(i in a){
		print a[i]","arr[i] | "sort -n";	
	}
}
' sample.txt covid_status.html > output1.txt
awk '{gsub(/[,]/," ", $0);print;}' output1.txt > output.txt
rm -rf output1.txt