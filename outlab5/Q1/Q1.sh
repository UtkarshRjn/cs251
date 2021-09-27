#!/bin/bash

sed -e 's/^/ /;s/$/ /' -e 's/[[:punct:]]\+//g' -e 's/[0-9]//g' -e 's/.*/\L&/' -e 's/http.[^ ]* \|https.[^ ]* \|www.[^ ]* //g'   \
 -e "$(sed 's:.*:s/ & / /ig:' stopwords.txt)" -e "$(sed 's:.*:s/& /$ /ig:' suffixes.txt)" -e's/$ / /g' -e 's/ .. / /g;s/ . / /g' -e 's/ .. / /g;s/ . / /g' -e's/ \+/ /g' -e 's/^ *//; s/ *$//' -e '/^$/d' sample.txt > output.txt