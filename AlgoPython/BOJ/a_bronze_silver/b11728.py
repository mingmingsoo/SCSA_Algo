n,m = map(int, input().split())
arr1 = list(map(int, input().split())) + list(map(int, input().split()))
arr1.sort()
print(*arr1)