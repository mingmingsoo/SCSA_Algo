'''
문제 설명
    이 길지만 전체 간선 합에서 최소간선길이를 빼라
입력
    간선정보인데 약간 귀찮은
출력
    전체 간선 합 - 최소 간선 길이
'''
import sys
input = sys.stdin.readline

V = int(input())

tmp = [list(input()) for i in range(V)]
edges = []
total_len = 0
for i in range(V):
    for j in range(V):
       if tmp[i][j] != "0":
           cost = 0
           if "a"<=tmp[i][j]<="z":
               cost = ord(tmp[i][j])-96
           else:
               cost = ord(tmp[i][j])-38
           edges.append((i, j, cost))
           total_len += cost

p = [v for v in range(V)]

edges.sort(key = lambda x:x[2])

min_len = 0
pick = 0

def find(x):
    if x!=p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x,y):
    p[find(y)] = find(x)

for i in range(len(edges)):
    px = edges[i][0]
    py = edges[i][1]

    if find(px) != find(py):
        # 대왕 부모가 다르면
        # 입양하기
        union(px,py)
        min_len += edges[i][2] # 그것이 최소길이
        pick+=1

    if(pick == V-1):
        break

# 모든 컴퓨터가 연결되어있지 않다는 것은...
# parent 들이 다르다는 것
idx = 0
for i in range(1, V):
    if(find(idx) != find(i)): # 대왕 부모를 비교!!!!!!!!!!!!!!!
        print(-1)
        break
else:
    print(total_len-min_len)