total = 0
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if(a<0):

    total += abs(a)*c
    total += d
    total += b*e
else:
    total += (b-a)*e

print(total)