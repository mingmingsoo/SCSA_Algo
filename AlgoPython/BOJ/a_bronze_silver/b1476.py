arr = [1,1,1]
rlt = list(map(int, input().split()))
ans = 0
for i in range(1,15*28*19+1):
    if(arr == rlt):
        ans = i
        break
    else:
        arr[0] = (arr[0]+1)%15
        arr[1] = (arr[1]+1)%28
        arr[2] = (arr[2]+1)%19
        if(arr[0]==0):
            arr[0] = 15
        if (arr[1] == 0):
            arr[1] = 28
        if (arr[2] == 0):
            arr[2] = 19


print(i)