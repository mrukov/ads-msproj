#/usr/bin/env zsh

PICTURE=$1
SLEEPTIME=$2
RESOLUTION=$3

(feh --hide-pointer -x -q -D 5 -B black -g $RESOLUTION $PICTURE) & pid=$!

(sleep $SLEEPTIME && kill -9 $pid) &

