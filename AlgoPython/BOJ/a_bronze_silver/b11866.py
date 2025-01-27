from collections import deque

n , k = map(int, input().split())
arr = deque()
for i in range(1,n+1):
    arr.append(i)
# print(arr)
list = []
while len(arr) > 0:
    for i in range(0, k-1):
        arr.append(arr[i])
    for i in range(0, k-1):
        del arr[0]
    list.append(arr.popleft())
# print(list)
print("<",end="")
for idx, num in enumerate(list):
    if(idx == len(list)-1):
        print(num, end="")
    else:
        print(num,end=", ")
print(">",end="")