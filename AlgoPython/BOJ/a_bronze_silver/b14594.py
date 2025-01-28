n = int(input()) # 동아리방 갯수
m = int(input()) # 빌런 횟수
arr = [1]*n
for i in range(m):
    start, end = map(lambda x: int(x)-1, input().split())
    for j in range(start, end):
        arr[j] = 0
print(arr.count(1))