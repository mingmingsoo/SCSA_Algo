'''
b16398

문제 설명
    이 길지만 결론적으로 MST를 구해라
입력
    가중치 정보들
출력
    MST
'''
import sys
input = sys.stdin.readline

V = int(input())
edges = []

tmp = [list(map(int, input().split())) for i in range(V)]

for i in range(V):
    for j in range(V):
        if(j>i):
            edges.append((i,j,tmp[i][j])) # 필요한 정보만 담기

edges.sort(key=lambda x:x[2])

p = [v for v in range(V)] # 0 부터
ans = 0
pick = 1
def find(x):
    if x!= p[x]:
        p[x] = find(p[x])
    return p[x]
def union(x,y):
    p[find(y)] = find(x) # y의 대왕부모를 x의 대왕부모로 바꾸기.

for i in range(len(edges)):
    px = edges[i][0]
    py = edges[i][1]
    if find(px) != find(py):
        # 우리의 대왕 부모가 다르면
        union(px,py) # 입양하기
        ans += edges[i][2]
        pick+=1
    if(pick == V):
        break
print(ans)