#!/bin/bash
startIndex=597998
endIndex=598058
formattedFilesDirPath="/home/pranav/Documents/Dropbox/Cricket/Formatted/"

for i in `seq $startIndex $endIndex`;
do
	inn1File=$formattedFilesDirPath$i"_Inn1.json"
	inn2File=$formattedFilesDirPath$i"_Inn2.json"
	mongoimport --collection matches --file $inn1File --db ipl_db --type json --jsonArray
	mongoimport --collection matches --file $inn2File --db ipl_db --type json --jsonArray
done
