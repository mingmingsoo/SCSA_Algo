'''
문제설명
    최소 개수의 동전을 옮겨서 새로운 모양을 만든다
구상
    이야 이거 어케하냐
     같은 모양이면 0 임
     1. 같은 모양인지 검사.
     2. 최소 동전 갯수는 합쳤을 때 안 겹쳐지는 애들임

     # 0이 시작되는 애들 정보를 담아..?
'''

n1, m1 = map(int, input().split())
grid1= [list(input()) for i in range(n1)]


n2, m2 = map(int, input().split())
grid2= [list(input()) for i in range(n2)]

def find(grid,n,m):
    sx, sy = 11,11
    ex, ey = -1,-1
    for i in range(n):
        for j in range(m):
            if grid[i][j]== "O":
                sx = min(sx,i)
                sy = min(sy,i)
                ex = max(ex,i)
                ey = max(ey,i)
    return sx,sy,ex,ey

sr1,sc1,er1,ec1 = find(grid1,n1,m1)
sr2,sc2,er2,ec2 = find(grid2,n2,m2)

# 맵 축소과정
arr1 = [[0]*(ec1-sc1+1) for i in range(er1-sr1+1)]
arr2 = [[0]*(ec2-sc2+1) for i in range(er2-sr2+1)]


for i in range(sr1,er1+1):
    for j in range(sc1,ec1+1):
        arr1[i][j] = grid1[i-sr1][j-sc1]


for i in range(sr2,er2+1):
    for j in range(sc2,ec2+1):
        arr2[i][j] = grid2[i-sr2][j-sc2]

# 필요한 가로 길이

