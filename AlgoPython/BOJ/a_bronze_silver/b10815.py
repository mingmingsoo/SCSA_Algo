n = int(input())
size = 10_000_000

have = list(map(lambda x: int(x)+size, input().split()))
m =  int(input())
doyouhave =list(map(lambda x: int(x)+size, input().split()))

arr = [0]*(2*size+1)

for num in have:
    arr[num] = 1

for num in doyouhave:
    print(arr[num], end = " ")