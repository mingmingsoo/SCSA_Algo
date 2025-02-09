m = int(input())
arr = [1,0,0]

for i in range(m):
    before, after = map(lambda x: int(x)-1, input().split())
    arr[before], arr[after] = arr[after], arr[before]

print(arr.index(1)+1)
