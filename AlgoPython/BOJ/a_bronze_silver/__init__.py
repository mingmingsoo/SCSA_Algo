'''
흠
'''

n = int(input())
memory = list(map(int, input().split()))
# 모르겠다.
# 순열 가자.
sel = [0]*n
visited = [False]*n

def perm(idx):
    if idx == n:
        print(sel)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            sel[idx] = i+1
            perm(idx+1)
            visited[i]= False



perm(0)