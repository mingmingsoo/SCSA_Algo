'''
리프노드: 자식이 없는 말단애들.
특정 노드 하나를 지울 떄 모든 자손이 트리에서 제거됨.
리프노드의 갯수는?

1. 내 자식들을 지우고,
2. 내가 지워져서 내 부모가 말단이 될 수도 있으니 부모 자식에서 날 지워줌.
'''

V = int(input())
tmp = list(map(int, input().split()))
parent_adj = [[] for i in range(V)]
child_adj = [[] for i in range(V)]

for i in range(V):
    parent = tmp[i]
    if parent != -1:
        child_adj[parent].append(i)
        parent_adj[i].append(parent)

delete = int(input())

deleteList = [False] * V
deleteList[delete]= True # 나도 잘릴거임

# 자식들 잘라줄거임
def dfs(delete):
    for node in child_adj[delete]:
        deleteList[node] = True
        dfs(node)

dfs(delete)

# 내 부모가 말단이 될 수 도있으니 내 부모에서 나를 지워주겠음
for node in parent_adj[delete]: # 내 부모들 자식중에
    for child in child_adj[node]: # 그 자식들 여러명 중에
        if( child == delete): # 나를 지워줄거임. ㅠㅠ
            child_adj[node].remove(child)

ans = 0

# 남은 애들 중에 (나 때문에 안잘라졌고) 말단인 애들 계산.
for i in range(V):
    if(not deleteList[i] and not child_adj[i]):
        ans+=1
print(ans)