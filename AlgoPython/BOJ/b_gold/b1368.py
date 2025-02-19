'''
b1368

문제 설명
    물 내가 풀래 VS 다른데서 끌어올래...

구상
    MST 를 구하되, 셀프로 물을 푸는것에 대한 값의 비교가 필요
    -> 무조건 우물 한번은 파야되므로 임의의 우물점을 설정해서 간선을 추가한다.
'''

V = int(input())
self = [int(input()) for v in range(V)]

tmp = [list(map(int, input().split())) for v in range(V)]

edges = []

for i in range(V):
    edges.append((0,i+1,self[i])) # 우물점 추가

for i in range(V):
    for j in range(V):
        if(j>i):
            edges.append((i+1,j+1,tmp[i][j])) # 필요한 정보만 받기

p = [v for v in range(V+1)]
pick = 0
ans = 0
edges.sort(key = lambda x:x[2])
def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x,y):
    p[find(y)] = find(x)

for i in range(len(edges)):
    px = edges[i][0]
    py = edges[i][1]

    if find(px) != find(py):
        union(px,py)
        ans += edges[i][2]
        pick+=1

    if pick == V:
        break

print(ans)
