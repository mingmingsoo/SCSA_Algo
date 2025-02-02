'''
문제 시작 15:00
문제 종료 15:40
- 문제 설명
4개의 톱니바퀴 정보와 회전횟수, 번호와 방향을 주어짐
톱니바퀴 정보는 12시 방향부터 시계방향 순서대로 주어짐(N-0, S-1)
회전 정보는 인덱스(1~4 : 1뻬줘야함)와, 방향을 줌(1:시계, -1:반시계)

- 회전이 가능한가?
i번째 톱니를 회전시킬 때 i+1번째 톱니와 맞닿은 극이 다르면  i+1은 반대방향으로 회전.  (-1 곱하기)
같은 극이면 회전하지 않음.
i 번째 기준으로 좌, 우 모두 확인해줘야함.

필요한 메서드
1. check: i번째 톱니를 회전시킬 때 다른 톱니들이 회전 가능한지, 불가능한지 체크(불리언 배열과, 방향을 담는 배열 필요)
2. rotation: 체크한 정보들로 회전.
3. score: 점수 계산

필요한 변수
1. 톱니바퀴 정보를 받은 2차원배열
2. 회전할 수 있는지 정보를 담는 1차원 배열
3. 회전는 방향을 담는 1차원 배열
'''

grid = [[] for i in range(4)]

for i in range(4):
    grid[i] = list(map(int, input()))

cnt = int(input())


def check(idx, dir):  # 움직일 수 있는지 체크하는 로직.
    # 왼쪽 체크.
    dirLeft = dir
    curLeft = grid[idx][6]
    for i in range(idx - 1, -1, -1):
        if (curLeft == grid[i][2]):
            break  # 같은 방향이면 더 왼쪽에 있는 애들도 못움직임
        else:
            rotation_list[i] = True
            dir_list[i] = (dirLeft * (-1))
            curLeft = grid[i][6]
        dirLeft *= -1  # 더 왼쪽으로 검사할 수 있으면 방향 바꿔주기

    # 오른쪽 체크
    dirRight = dir
    curRight = grid[idx][2]
    for i in range(idx + 1, 4):
        if (curRight == grid[i][6]):
            break
        else:
            rotation_list[i] = True
            dir_list[i] = (dirRight * (-1))
            curRight = grid[i][2]
        dirRight *= -1


def roro(i):
    # 시계방향으로 회전
    # [0,1,2,3] -> [3,0,1,2]
    copyGrid = grid[i][:]
    rogGrid = [copyGrid[-1]]
    rogGrid += copyGrid[:7]
    grid[i] = rogGrid[:]


def lele(i):
    # 시계방향으로 회전
    # [0,1,2,3] -> [1,2,3,0]
    copyGrid = grid[i][:]
    rogGrid = copyGrid[1:]
    rogGrid += [copyGrid[0]]
    grid[i] = rogGrid[:]


def rotation():
    for i in range(4):
        # 회전 가능하면 회전시켜줌
        if (rotation_list[i]):
            d = dir_list[i]
            if (d == 1):
                roro(i)
            else:
                lele(i)

def score():
    total = 0
    num = 1
    for row in grid:
        if (row[0] == 1):
            total += num
        num *= 2
    return total


for c in range(cnt):
    idx, dir = map(int, input().split())
    idx -= 1

    rotation_list = [False] * 4
    dir_list = [0] * 4
    rotation_list[idx] = True
    dir_list[idx] = dir
    check(idx, dir)  # 회전 가능한지 확인하고 위 두 리스트에 정보를 담음

    # print(rotation_list)
    # print(dir_list)
    rotation()
    # for ele in grid:
    #     print(ele)
    ans = score()
print(ans)
