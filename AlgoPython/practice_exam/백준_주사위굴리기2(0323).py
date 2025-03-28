'''
# 0322 2회차 풀이
# 코드트리 2개의 사탕 (백준 구슬탈출2)
# 체감난이도 골2~골3

# 문제 풀고 나서 기록
    제출횟수 1회
    문제 시작 19:34
    문제 종료 20:00
    총 풀이시간 26분
        34~40   : 문제 이해, 초기 주석, 문제 구상, 입력받기(6)
        40~50   : bfs 로직 설계(10)
                    - 초기 주석으로 적어둔 성공 / 실패 조건 코드 먼저 작성
                    - 공 움직이는 로직 / 공 겹쳐질때 / 위치바뀔 때만 q에 넣어주는 코드 짜기
                        (여기서 공 겹쳐질 때 next_red_r을 수정해야하는데 red_r 을 +=1 해주고있음..)
                    - 공 움직이는 move 함수 작성
        50~00   : 인덱스 에러나서 디버깅
                    1.move 함수(3)
                        nbr, nbc = move(rr,rc)로 되어있어서
                        nbr, nbc = move(br,bc)로 수정
                        -> 그래도 인덱스 에러!
                    2. q에서 pop하는 애들 찍어보니까(6)
                        겹쳐지는 애들은 구멍에 빠질때 빼고는 없는데 (4,4),(4,4) 가 나옴!
                        허튼데 디버깅하다가... 겹쳐지는 애들 값 수정해주는 로직에서 변수를 잘못썼네.. 수정!
                        next_red_r을 ->  red_r

    - visited 쓰면
        메모리 19 KB
        시간 91 ms
    - visited 안쓰면
        메모리 16 KB
        시간 49 ms

    회고
        1. visited 로직도 추가하니까
            -> 시간 91ms에서 49ms로 줄어듬
        2. 구슬탈출 1~4까지 풀어서 3회차 풀이는 안해도 괜찮을 것 같다.
        3. 구슬 움직이는 로직을 함수화로 처음부터 하니까 코드짜기가 편했다! 설계를 합시다!
        4. 변수가 길어지니까 좀 불편해서... nrr, nrc 이렇게 쓰면 좀 더 좋을 듯??

# 문제 풀면서의 기록

코드트리 정육면체 굴리기 1626~16:46
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
