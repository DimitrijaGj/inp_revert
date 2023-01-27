#!/usr/bin/env python

#01 42 44 46 CB 5C 80 - secureprint
#805CCB46444201 - siport
siport='805CCB46444201'
secprnt='01424446CB5C80'
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
final=pr7[:2]+pr6+pr5+pr4+pr3+pr2+pr1
#print(final)
if final==siport:
    print(final)
else:
    print('The strigs are not equal')
#print(type(whole))

#print(pr7[:2],pr6,pr5,pr4,pr3,pr2,pr1)
#print(whole)