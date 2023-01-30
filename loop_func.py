#!/usr/bin/env python
import sys

#01 42 44 46 CB 5C 80 - secureprint
#805CCB46444201 - siport
siport='805CCB46444201'
secprnt='01424446CB5C80'
result =[]
for i in range(0, len(siport), 2):
    result.append(siport[i:i+2])
print(result)
#the loop goes from 0 to len of the string , every second number, 0,14,2,
#and we use that to slice the string siport[0:2] second run siport[2:4] etc. 
#and gives list at the end
rev_res=result[::-1]
#hre we reverse the list order
fin_result=''.join(rev_res)
#we creating one sring from all the strings in the list
if fin_result==secprnt:
    print(fin_result, 'Opperation was succesfull')
else:
    print('The generated string does not match')
#adding some checking points if strings are matching

    