'''
[문제 설명]
    치킨집을 폐업시키는데 전체 치킨 - 집 사이의 거리가 가깝게 폐업시켜라
    ㅠㅠ

[입력]
    맵 크기n, 치킨집 몇개m 남길 것인지
    맵
[출력]
    치킨집과의 전체 거리.

[구상]
    치킨집들 중에 m개를 선택 -> 조합 (위치를 담기도 해야함)
    조합 한 후에 전체 거리를 구해서 치킨 거리가 작게끔 갱신한다.

[시간복잡도]
    맵을 탐색하는 N^2 + 조합 전체치킨 C M

'''

n, m = map(int,input().split())
grid =  [list(map(int, input().split())) for i in range(n)]
kokos = []
houses = []

# 치킨집 정보 담기
ko_num = 0 # 치킨집 번호
house_num = 0 # 집 번호 : 번호 남기는 이유는 내 편의를 위해,, 디버깅을 위해
for i in range(n):
    for j in range(n):
        if(grid[i][j] == 2):
            kokos.append((ko_num, i,j))
            ko_num+=1
        elif(grid[i][j] == 1):
            houses.append((house_num, i,j))
            house_num+=1

# print(kokos)
# print(houses)
arr = list(range(ko_num)) # 전체 치킨집 번호
sel = [0]*m # 선택할 치킨집 번호를 담을 배열
ans = 50*50*13+1

def cal(sel):
    dist = 0
    for house_num, hr, hc  in houses:
        ele_dist = 50*50*13+1
        for idx in sel:
            ko_num, kr, kc = kokos[idx]
            ele_dist = min(abs(hr-kr)+ abs(hc-kc),ele_dist)
        dist+=ele_dist
    return dist
def combi(sidx,idx):
    global ans
    if(sidx ==m):
        ans = min(cal(sel),ans)
        return

    if(idx ==ko_num):
        return

    sel[sidx] = arr[idx]
    combi(sidx+1,idx+1)
    combi(sidx, idx+1)

combi(0,0)
print(ans)