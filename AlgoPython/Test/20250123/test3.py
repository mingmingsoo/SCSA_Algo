L = int(input())
N = int(input())
arr = [0]*L
originMax = 0
originIdx = 0
for i in range(N):
    start, end = map(lambda x:int(x)-1, input().split())
    if(originMax < (end-start)):
        originMax = end-start
        originIdx = i+1
    for j in range(start, end+1):
        if(arr[j]==0):
            arr[j] = i+1
# print(arr)

count = [0]*N
for i in range(0, L):
    if(arr[i]!=0):
        count[arr[i]-1] += 1
ansIdx = 0
# print(count)
for i in range(0,N):
    if(count[i]==max(count)):
        ansIdx = i+1
        break
print(originIdx)
print(ansIdx)