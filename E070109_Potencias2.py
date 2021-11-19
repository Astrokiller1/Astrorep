import math 
import sys

def multiplica2_range(start, stop):
    while start < stop:
        yield start
        start <<= 1

def divide2_range (start, stop):
    while start > stop:
        yield start
        start >>= 1
        
print("Primeira aproximação : ")
for i in multiplica2_range(1,1025):
    print(i)

print("Segunda aproximação : ")
for i in divide2_range (1024,0):
    print(i)