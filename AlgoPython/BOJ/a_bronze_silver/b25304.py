total = int(input())
n = int(input())
compare = 0
for i in range(0,n):
    a, b = map(int, input().split())
    compare += (a*b)
if(total == compare):
    print("Yes")
else:
    print("No")
