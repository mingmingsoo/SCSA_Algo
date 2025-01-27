arr = [0]*11

arr[0]=1
arr[1]=1
arr[2] =2
for i in range(3,11):
        arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
T = int(input())
for t in range(T):
    n = int(input())
    print(arr[n])