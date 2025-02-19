'''
union-find 연습
몇개의 그룹인가?를 찾는다
# 부모가 총 몇명인가?

'''

def find(x): # 너 진짜 부모가 누구야??
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y): # y를 x가족에 포함시켜버리기
    p[find(y)] = find(x) # y의 부모를 x의 대왕 부모로 바꿀게요

T = int(input())
for tc in range(T):

    V, E = map(int, input().split())
    tmp = list(map(int, input().split()))

    p = [n for n in range(V + 1)]

    for i in range(0, E * 2, 2):
        union(tmp[i], tmp[i + 1]) # 가족 구성원 만들기

    parent = 0
    for i in range(1, V + 1):
        if i == p[i]: # 총 부모가 몇명인지 세주기
            parent += 1

    print(f"#{tc+1} {parent}")

