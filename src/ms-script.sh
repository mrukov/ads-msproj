#/usr/bin/env zsh

PATH=$1
SLEEPTIME=$2
RESOLUTION=$3
FILENUMBER=$4

FILE=""

count=0

for entry in $PATH/*
do
    if (( $count == $FILENUMBER )); then
        FILE=$entry
    fi
    count=$((count+1))
done

(/usr/bin/feh --hide-pointer -x -q -B black -g $RESOLUTION $FILE) & pid=$!
(/usr/bin/sleep $SLEEPTIME && kill -9 $pid) 

