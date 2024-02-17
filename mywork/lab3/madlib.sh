#!/bin/bash

clear
echo "Let's build a mad-lib!"

read -p "1. Please give me an adjective: " ADJ1
read -p "2. Please give me a noun: " NOUN1
read -p "3. Please give me a verb: " VERB1
read -p "4. Please give me an adverb: " ADV1
read -p "5. Please give me another adjective: " ADJ2
read -p "6. Please give me another noun: " NOUN2
read -p "7. Please give me another verb: " VERB2
read -p "8. Please give me another adverb: " ADV2

echo "Once upon a time, in a land far, far away, there was a $ADJ1 $NOUN1. It loved to $VERB1 $ADV1."
echo "One day, it met a $ADJ2 $NOUN2 that also loved to $VERB2 $ADV2. They became the best of friends and had many adventures together."
echo "The end."
