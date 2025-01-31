n,m = map(int, input().split())

k = int(input())

xlist = [0]
ylist = [0]
for i in range(k):
    dir, idx = map(int, input().split())
    if(dir == 0):
        xlist.append(idx)
    else:
        ylist.append(idx)

xlist.sort()
ylist.sort()
xlist.append(m)
ylist.append(n)
x = []
y = []
# print(xlist)
# print(ylist)
for i in range(len(xlist)-1,0,-1):
    x.append(xlist[i]-xlist[i-1])
for i in range(len(ylist)-1,0,-1):
    y.append(ylist[i]-ylist[i-1])
# print(x)
# print(y)
ans = 0
for i in range(len(x)):
    for j in range(len(y)):
        ans = max(ans, x[i]* y[j])
print(ans)