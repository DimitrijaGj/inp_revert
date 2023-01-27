#!/usr/bin/env python

import sys
#takes input fro user script.py [input from user] in form of string
secprnt=str(sys.argv[1])
#explode srt in pairs
pr1=secprnt[0:2]
pr2=secprnt[2:4]
pr3=secprnt[4:6]
pr4=secprnt[6:8]
pr5=secprnt[8:10]
pr6=secprnt[10:12]
pr7=secprnt[12:15]
#whole=pr1+pr2+pr3+pr4+pr5+pr6+pr7
#invert=pr7[:2]
#print(invert)
#puting pairs together with inverting the last pair
final=pr7[:2]+pr6+pr5+pr4+pr3+pr2+pr1
print(final)