n = int(input())
arr = []

for _ in range(n):
    kg, cm = map(int, input().split())
    arr.append([kg,cm])

for i in range(n):
    big = 1
    for j in range(n):
        if(i==j):
            continue
        if(arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]):
            big+=1
    print(big, end=" ")