from itertools import count

x=0
p=0

for x in (3**p for p in count(1)):
    if (x > 1000):
        break
    else: print(x)