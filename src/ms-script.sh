#/usr/bin/env zsh

PATH=$1
SLEEPTIME=$2
RESOLUTION=$3
FILENUMBER=$4

FILE=""

count=0

echo $FILENUMBER

for entry in $PATH/*
do
    echo $entry
    if (( $count == $FILENUMBER )); then
        FILE=$entry
    fi
    count=$((count+1))
done

echo $FILE

(feh --hide-pointer -x -q -B black -g $RESOLUTION $FILE) & pid=$!
(sleep $SLEEPTIME && kill -9 $pid) 

