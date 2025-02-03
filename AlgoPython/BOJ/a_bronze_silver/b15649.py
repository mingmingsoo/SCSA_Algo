'''
중복순열 아니고 그냥 순열 출력
'''
n, m = map(int, input().split())

arr = list(range(1, n + 1))
arr.sort()
# 혹은 arr = [i for i in range(1, n+1)]

sel = [0] * m

visited = [False] * n


def perm(sidx, idx):
    if (sidx == m):
        print(*sel)
        return
    if (idx == n):
        return
    for i in range(n):
        if (not visited[i]):
            sel[sidx] = arr[i]
            visited[i] = True
            perm(sidx + 1, idx + 1)
            visited[i] = False


perm(0, 0)  # sidx
