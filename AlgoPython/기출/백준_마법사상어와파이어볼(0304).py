'''
# 코드트리 원자 충돌 (백준 20056 마법사 상어와 파이어볼)

# 문제 풀고 나서 기록

    문제 시작 09:00
    문제 종료 10:06
    총 풀이시간 66분
        0~4분    : 문제 이해(4)
        4~7분    : 문제 구상 및 초기 주석(3)
        7~11분   : 탑다운 설계(4)
        11~18분  : 범위 헷갈렸던거 지문에서 찾고, ele_move 설계 완료(7)
        18~33분  : is_double 1차 설계 -> 남은애들 4갠데 5개 나와서 1차 디버깅(15)
        33~56분  : is_double 1차 디버깅 완료(23)
        56~57분  : is_remove 함수 설계(1)
        57~66분  : 인덱스를 어떻게 처리할지 고민하다가 isOut 불리언 배열 만듬(9)

    1. 첫번째 풀이
    메모리 125756 KB
    시간 2548 ms

    2. 두번째 풀이
    메모리 125876 KB
    시간 308 ms

    회고 :
        1.
        참 많은 것을.... 알게한 소중한 문제... ★일차원배열로 풀거면 시간복잡도 계산하고 풀기★

        2.
        첫번째 풀이에서 내 코드 시간복잡도가 큰 이유:
            이차원배열로 관리하면 N*N(50*50)
            근데 나는 M*M(50*50*50*50)
            운이 좋아서 첫번째 코드는 통과한거임.
             4 ≤ N ≤ 50
             0 ≤ M ≤ N^2
            -> 귀찮아도 2차원 배열로 관리했었어야함.

        3.
        고민되는점 : 이동시 범위를 벗어나면 어떻게 되는거지? 아 연결되어있다고 써있음 이라고 초기주석에 썼었음.
        -> 절대 문제에 필요없는데 써있는말은 없다.
        "격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다." 를 읽고 처음엔 그냥 엥?뭔소리지 넘겼었는데 이 말이 정보였음.

        4.
        is_double에서 애먹었던거
        remove 해주면 인덱스가 밀리는데... 그러면 다음 탐색이 어려워져서 is_out을 썼음
        만약 합쳐지면 is_out True처리하고, is_out이 True인 애들은 인덱스가 넘어가게했음.
        이거 생각하느라 시간이 많이 걸렸다....
        ★remove 해주기보단 새로운 배열에 넣고 그걸 복사하는게 편하다★

        5.
        클래스 사용익히자. 너무 편하다.

문제설명
    파이어볼은 각자의 속성이 있다.
    이동 후 두개 이상의 파이어볼이 있는 칸이라면
        1. 합쳐진다.
        2. 파이어볼은 4개로 나누어진다.
        3. 홀짝에 따라 흩어지는 위치가 다르다.
        * 질량이 0이면 소멸된다.
    k번 이동후 남아있는 질량의 합은?
입력
    맵크기 N, 파이어볼 M, 이동 횟수 move
    파이어블 r,c,m,s,d

필요한 메서드
    ele_move : 각자 움직임
    is_double : 합쳐지는거 확인, 흩뿌리기

고민되는점
    이동시 범위를 벗어나면 어떻게 되는거지?
    아 연결되어있다고 써있음

'''


#################################################################
# 첫번째 풀이, 운좋아서 통과 자칫하면 시초임

def ele_move():
    for i in range(len(ball_list)):
        r, c, mass, s, d = ball_list[i]
        nr = (r + row[d] * s + n) % n
        nc = (c + col[d] * s + n) % n

        ball_list[i][0] = nr
        ball_list[i][1] = nc


# 범위 확인하기 # 아마 이게 뒤에서부터 되야할거임..
def is_double():
    global ball_list
    new_ball_list = []
    isout = [False] * len(ball_list)
    for i in range(len(ball_list) - 1, -1, -1):
        if isout[i]:
            continue
        r1, c1, mass1, s1, d1 = ball_list[i]
        same_idx = [(r1, c1, mass1, s1, d1, i)]
        for j in range(i - 1, -1, -1):
            r2, c2, mass2, s2, d2 = ball_list[j]
            if r1 == r2 and c1 == c2:
                same_idx.append((r2, c2, mass2, s2, d2, j))

        if (len(same_idx) > 1):
            new_mass, new_s = 0, 0
            d_list = []

            for i in range(len(same_idx)):
                r, c, mass, s, d, idx = same_idx[i]
                new_mass += mass
                new_s += s
                d_list.append(d % 2)
                isout[idx] = True
                # ball_list.pop(idx)

            new_r, new_c = same_idx[0][0], same_idx[0][1]
            new_mass //= 5
            new_s //= len(same_idx)

            if d_list.count(1) == len(same_idx) or d_list.count(0) == len(same_idx):
                new_ball_list.append([new_r, new_c, new_mass, new_s, 0])
                new_ball_list.append([new_r, new_c, new_mass, new_s, 2])
                new_ball_list.append([new_r, new_c, new_mass, new_s, 4])
                new_ball_list.append([new_r, new_c, new_mass, new_s, 6])
            else:
                new_ball_list.append([new_r, new_c, new_mass, new_s, 1])
                new_ball_list.append([new_r, new_c, new_mass, new_s, 3])
                new_ball_list.append([new_r, new_c, new_mass, new_s, 5])
                new_ball_list.append([new_r, new_c, new_mass, new_s, 7])

    for i in range(len(isout)):
        if not isout[i]:
            r, c, mass, s, d = ball_list[i]
            new_ball_list.append([r, c, mass, s, d])
    ball_list = new_ball_list


def is_remove():
    for i in range(len(ball_list) - 1, -1, -1):
        r1, c1, mass1, s1, d1 = ball_list[i]
        if mass1 == 0:
            ball_list.pop(i)


n, m, move_num = map(int, input().split())
ball_list = []
for i in range(m):
    r, c, mass, s, d = map(int, input().split())
    r -= 1
    c -= 1
    ball_list.append([r, c, mass, s, d])
# print(ball_list)

row = [-1, -1, 0, 1, 1, 1, 0, -1]
col = [0, 1, 1, 1, 0, -1, -1, -1]

for move in range(move_num):
    ele_move()
    is_double()
    is_remove()

ans = 0
for r, c, mass, s, d in ball_list:
    ans += mass

print(ans)


#################################################################
# 두번째 풀이 2차원배열로, 클래스 사용

class Ball:
    def __init__(self, mass, s, d):
        self.mass = mass
        self.s = s
        self.d = d


def ele_move():
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                for ball in grid[i][j]:
                    nr = (i + row[ball.d] * ball.s) % n
                    nc = (j + col[ball.d] * ball.s) % n
                    new_grid[nr][nc].append(Ball(ball.mass, ball.s, ball.d))


def is_double():
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) > 1:
                new_mass = 0
                new_s = 0
                all_eve_odd = True
                first_d = grid[i][j][0].d % 2
                if first_d > 1:
                    all_eve_odd = False

                for ball in grid[i][j]:
                    if ball.d % 2 != first_d:
                        all_eve_odd = False
                    new_mass += ball.mass
                    new_s += ball.s

                new_mass //= 5
                new_s //= len(grid[i][j])
                grid[i][j] = []  # 빈리스트 만들어주고
                if new_mass <= 0:
                    continue
                if all_eve_odd:
                    grid[i][j].append(Ball(new_mass, new_s, 0))
                    grid[i][j].append(Ball(new_mass, new_s, 2))
                    grid[i][j].append(Ball(new_mass, new_s, 4))
                    grid[i][j].append(Ball(new_mass, new_s, 6))
                else:
                    grid[i][j].append(Ball(new_mass, new_s, 1))
                    grid[i][j].append(Ball(new_mass, new_s, 3))
                    grid[i][j].append(Ball(new_mass, new_s, 5))
                    grid[i][j].append(Ball(new_mass, new_s, 7))


n, m, move_num = map(int, input().split())
grid = [[[] for i in range(n)] for i in range(n)]
for i in range(m):
    r, c, mass, s, d = map(int, input().split())
    grid[r - 1][c - 1].append(Ball(mass, s, d))

row = [-1, -1, 0, 1, 1, 1, 0, -1]
col = [0, 1, 1, 1, 0, -1, -1, -1]

for t in range(move_num):
    new_grid = [[[] for i in range(n)] for i in range(n)]
    ele_move()
    grid = new_grid
    is_double()
ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            for ball in grid[i][j]:
                ans += ball.mass
print(ans)
