# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:36:26 2023

@author: Wilian
"""

S1 = (3/40) + (32/39) + (33/38) + (34/37) + (340/1) 
#print(S1)
S2 = (480/2) + (475/22) + (470/23) + (465/24) + (460/25)
x = 1
first = 460.0
second = 25.0
newS2 = 0.0
while True:
    x = x + 1
    if x == 21:
        break
    first = first - 5.0
    second = second - 1.0
    newS2 = newS2 + S2 + (first/second)
    newSoma2 = newS2
#print(newS3)
S3 = 1.0/2.0 + 3.0/23.0
first = 3.0
second = 23.0
y = 1
newS3 = 0.0
while True:
    y = y + 1
    if y == 20:
        break
    first = ((2.0**(y + 2)) - 1.0)
    second = second + 2.0
    #print(first,second)
    newS3 = newS3 + S3 + (first/second)
    newSoma3 = newS3
print(newSoma3)