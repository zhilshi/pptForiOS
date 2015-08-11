#! /bin/bash
imagesPath='/Users/appteam/Desktop/VideoGo@2.5/VideoGo/VideoGo/SupportingFiles/images'
dirPath='/Users/appteam/Desktop/VideoGo@2.5/VideoGo/VideoGo'

for i in `find "$imagesPath"  -name "*.png" -o -name "*.jpg"`;do
	file=`basename -s .jpg "$i" | xargs basename -s .png | xargs basename -s @2x`

	result=`ack -i "$file" "$dirPath"`
	if [ -z "$result" ]; then
#        echo "$i"
        rm "$i"
    fi
done

