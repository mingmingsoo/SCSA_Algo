'''
# 0323 2회차 풀이
# 코드트리 정육면체 굴리기 (백준 주사위 굴리기)
# 체감난이도 골3~골4

# 문제 풀고 나서 기록

    제출횟수 1회
    문제 시작 16:26
    문제 종료 16:46
    총 풀이시간 20분
        26~28   : 문제 이해(2)
        28~30   : 초기주석 및 문제 구상(2)
        30~35   : 주석으로 단 1,2,3을 3,1,2 로 설계 / 일단 3만 설계!
                    3. 격자판 밖으로 이동하라는 명령은 무시
                    1. 정육면체를 굴리는데 격자판이 0이면 주사위 바닥면에 쓰여있는 수가 격자판에 복사
                    2. 격자판이 0이아니면 칸에 쓰여있는 수가 주사위 바닥에 복사되고 그 칸은 0이됨
        35~42   : 주사위 굴리는 roll 설계 - index로(7)
        42~43   : 나머지 1,2 설계(1)
        43~45   : 인덱스 에러나서 디버깅(2)
                    roll 함수에서 dice를
                    [dice[4] + dice[5] + dice[2] + dice[3] + dice[1] + dice[0]]
                    더해버렸네... + 에서 , 로 수정
                    -> [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
        45~46   :   오잉 답이 안나오네?(1)
                    아 주사위 위치 바꿔주고 갱신해주는 코드가 없네!
                        r= nr, c = nc 추가!

    메모리 16 KB
    시간 60 ms

    회고
        1. 처음 주말 스터디에서 풀었을 땐 (주사위 바닥에 복사되고 그 칸은 0이됨) 이 조건을 놓쳐서 디버깅하는데 시간 오래걸렸었는데
            문제를 읽으면서 조건을 기록해둬서 이번엔 안놓치고 빨리 풀 수 있었다!
        2. 확실히 1회차 풀이보다 간단히 풀었네!!!

# 문제 풀면서의 기록
문제설명
    1. 정육면체를 굴리는데 격자판이 0이면 주사위 바닥면에 쓰여있는 수가 격자판에 복사
    2. 격자판이 0이아니면 칸에 쓰여있는 수가 주사위 바닥에 복사되고 그 칸은 0이됨
    3. 격자판 밖으로 이동하라는 명령은 무시

입력
    n,m 정육면체 처음위치 x,y, 굴리는 횟수 k
    격자판 정보
    1  2  3  4
    동 서 북 남
출력
    매 이동마다 주사위 상단에 쓰여있는 숫자 출력
구상
    성실히 구현....
'''

n, m, r, c, d_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
d_list = list(map(lambda x: int(x) - 1, input().split()))
row = [0, 0, -1, 1]
col = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]


#  0: 위 1: 밑 2: 앞 3: 뒤 4:왼 5:오
def roll(d):
    global dice
    if d == 0:
        dice = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
    elif d == 1:
        dice = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]
    elif d == 2:
        dice = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]
    elif d == 3:
        dice = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]


for d in d_list:
    # 3. 격자판 밖으로 이동하라는 명령은 무시
    if not (0 <= r + row[d] < n and 0 <= c + col[d] < m):
        continue
    nr = r + row[d]
    nc = c + col[d]

    # 1. 정육면체를 굴리는데 격자판이 0이면 주사위 바닥면에 쓰여있는 수가 격자판에 복사
    roll(d)
    if grid[nr][nc] == 0:
        grid[nr][nc] = dice[1]
    # 2. 격자판이 0이아니면 칸에 쓰여있는 수가 주사위 바닥에 복사되고 그 칸은 0이됨
    else:
        dice[1] = grid[nr][nc]
        grid[nr][nc] = 0
    r = nr
    c = nc
    print(dice[0])

'''
# 0209 1회차 풀이
# 백준 14499 주사위 굴리기
# 주말스터디에서 진행한 코드
'''
n, m, r, c, ORDER_NUM = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(n)]
order_list = list(map(lambda x: int(x) - 1, input().split()))
row = [0, 0, -1, 1]
col = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]  # 윗면,밑면,앞면,뒷면,왼쪽면,오른쪽면
ans = []

if (grid[r][c] != 0):
    dice[1] = grid[r][c]
    grid[r][c] = 0

for i in range(len(order_list)):

    d = order_list[i]
    ans.append(dice[0])
    nr = r + row[d]
    nc = c + col[d]
    if (not (0 <= nr < n and 0 <= nc < m)):
        ans.pop()
        continue
    if (d == 0):  # 동쪽이면
        new_dice = dice[4:] + dice[2:4] + [dice[1]] + [dice[0]]
        dice = new_dice[:]
        # print(dice[0])
    elif (d == 1):  # 서쪽이면
        new_dice = [dice[5]] + [dice[4]] + dice[2:4] + dice[:2]
        dice = new_dice[:]
    elif (d == 2):  # 북쪽이면
        new_dice = dice[2:4] + [dice[1]] + [dice[0]] + dice[4:]
        dice = new_dice[:]
    elif (d == 3):  # 남쪽이면
        new_dice = [dice[3]] + [dice[2]] + dice[:2] + dice[4:]
        dice = new_dice[:]

    if (grid[nr][nc] == 0):
        grid[nr][nc] = dice[1]
    else:
        dice[1] = grid[nr][nc]
        grid[nr][nc] = 0
    r = nr
    c = nc

ans.pop(0)
ans.append(dice[0])
for i in range(len(ans)):
    print(ans[i])
