import sys
import math
import msvcrt
import time

print("  Minutos Segundo Milisegundos : ")
for minutos in range(0,60,1):
    for segundos in range(0,60,1):
        for milisegundos in range(0,1000,1):
            print("   ", format(minutos,'3d'), "  ", format(segundos, '3d'),"  ", format(milisegundos), end="\r")
            if msvcrt.kbhit():
                break
        if msvcrt.kbhit():
            break
    if msvcrt.kbhit():
            break
print()
print("Cronómetro parado!!", end="")
print()