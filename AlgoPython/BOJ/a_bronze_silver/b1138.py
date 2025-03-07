'''
흠
'''

n = int(input())
memory = list(map(int, input().split()))
# 모르겠다.
# 순열 가자.
sel = [0]*n
visited = [False]*n
find = False
def perm(idx):
    global find
    if find:
        return
    if idx == n:
        arr = [0]*n
        for i in range(n):
            taller = 0
            for j in range(0,i):
                if sel[j]>sel[i]:
                    taller +=1
            arr[sel[i]-1] = taller
        if arr ==memory:
            print(*sel)
            find = True
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            sel[idx] = i+1
            perm(idx+1)
            visited[i]= False



perm(0)