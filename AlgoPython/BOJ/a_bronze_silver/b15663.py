import copy

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
ans = []

sel = [0]* m
visited = [False] * n

def cal(idx):
    if(idx >= m):
        # print(sel)
        ans.append(tuple(sel)) # 튜플로 받아야 set으로 변환할 수 있고 copy 도 안해도됨
        return
    for i in range(n):
        if(not visited[i]):
            sel[idx] = arr[i]
            visited[i] = True
            cal(idx+1)
            visited[i] = False





cal(0)
ans = list(set(ans))
ans.sort()
for ele in ans:
    for j in ele:
        print(j, end = " ")
    print()