n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
k = int(input())


def maleCal(idx):
    for i in range(idx,n+1,idx):
        arr[i] = 1-arr[i]


def femaleCal(idx):
    arr[idx] = 1-arr[idx]
    for plus in range(0,n+1):
        if(idx-plus<=0):
            break
        if(idx+plus>=n+1):
            break
        if(arr[idx+plus]!=arr[idx-plus]):
            break
        arr[idx + plus] = 1-arr[idx + plus]
        arr[idx - plus] = 1 - arr[idx - plus]

for i in range(k):
    sex, idx = map(int, input().split())
    if(sex==1):
        maleCal(idx)
    elif(sex==2):
        femaleCal(idx)

for ele in range(1,n+1):
    print(arr[ele], end= " ")
    if(ele % 20 ==0):
        print()
