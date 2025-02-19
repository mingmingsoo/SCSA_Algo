'''
b1717

문제 설명
    n+1 개의 집합이 있는데
    합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지 확인하는 연산
입력
    V 정점 , M 연산의 갯수
    합집합 0 a b
    같은 집합? 1 a b -> 이때 출력
'''

V, order = map(int, input().split())

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    p[find(y)] = find(x)

p = [v for v in range(V + 1)]

for o in range(order):
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        union(tmp[1], tmp[2])
    else:  # 1 이면
        if (find(tmp[1]) == find(tmp[2])): # parent에 바로바로 부모가 갱신되는게 아니라서... # 너의 대왕부모가 누구야? 를 찾아줘야함
            print("YES")
        else:
            print("NO")
