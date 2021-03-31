#!/bin/bash

if [ "$#" -ne 4 ]
then
    echo "$0 <высота> <ширина> <закрасить прямоугольник или нет (0\1)> <символ(ы) рисования рамки>"
    exit 1
fi

H=$1
W=$2
if [ $3 -eq 0 ]
then
    FILLCH=' '
else
    FILLCH='*'
fi

for (( i = 1; i <= $H; i++ )); do
  for (( j = 1; j <= $W; j++ )); do
    if (( 1 == i || $H == i || 1 == j || $W == j )); then
      echo -n $4
    else
      echo -n "$FILLCH"
    fi
  done
  echo
done
