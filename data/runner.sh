#!/bin/bash
input=$1
while IFS= read -r line
do
  python "$line"
done < "$input"