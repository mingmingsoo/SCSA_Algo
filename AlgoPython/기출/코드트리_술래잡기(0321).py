'''
# 코드트리 술래잡기
# 체감난이도 골1~골2

# 문제 풀고 나서 기록

    문제 시작 09:02
    문제 종료 11:08
    총 풀이시간 128분
        02~12   : 문제 이해(10) (화장실 3분)
        12~19   : 초기 주석 및 문제 구상(7)
                    도망자들 1차원으로 관리할 까하다가 n^2이길래 3차원 배열로 짰음
        19~23   : 입력받기(4)

        23~34   : [달팽이 로직 구현](11)
                  움직여야 하는 방향을 2차원 배열로 미리 담아뒀음
                  (중앙 -> 끝으로 갈때 / 끝 -> 중앙으로 갈 때)
                  -> 여기서 문제 생길 예정

        34~39     : [도망자 이동 로직 구현]

        39~46     : [술래잡기 로직 구현]
                    술래 이동 방향은 기존 r,c에서 방향 2차원배열의 값으로 이동하고
                    술래 시야 방향은 이동한 방향인 nr,nc 의 2차원배열의 값을 가져야함.

        46~56      : 로직 완료, 테케 검증 시작
                    - 테케 1번,3번 검증(1,3은 턴 수만 다름)
                        1. 도망자 이동 방향 배열 수정 (0,-1,0,1) -> (0,1,0,-1)
                        2. 술래가 3칸 바라본다는 것은 본인 위치 포함임!
                            나는 본인 미포함 3칸이여서 for문 range 수정
                    - 테케 2번 검증
                        1. 도망자가 술래와 거리가 3초과일 때 new_grid에 안넣어줘서 수정!! 휴... 바보냐? 자꾸 이러네

        56~26     : 테케는 턴 수가 적기에 턴수 30으로 늘려서 넣어봄(30)
                    !!!!!!인덱스 에러!!!!!!
                    1. 이유로는 중앙 -> 끝으로의 방향배열은 잘 담겼으나
                        끝-> 중앙 배열이 문제였음
                        이걸 알아차리는데 많은 시간이 걸렸다....
                        애꿎은 change 변환 로직만 두둘겨팼음
                    2. 문제를 풀어야된다는 급한 마음에 기존 달팽이 로직에서 순서만 쩨끔 바꾸면 되는걸
                        끝 -> 중앙용 달팽이 로직을 짰음(visited 쓰는) - 이건 손에 익어서 빨리 짰다.
                        뭐 해결했으니 다행이다만 침착히 생각했으면 간단한 일인데 말이다.

  메모리 17 KB
  시간 57 ms


    회고
        1. 구상도 잘했고 설계도 잘 했음
        2. 검증용 테케 돌리다가 인덱스 에러나서 당황해서 버버벅 하다가 시간 많이 끈듯
            -> 잘한건 스스로 돌려봤다는 것?
        3. 처음부터 달팽이 잘 확인하고 들어갔으면 덜 버벅였을텐데 싶다.


# 문제 풀면서의 기록

문제설명
    - 나무는 가림용이다.
    - 게임
        1. 도망 (술래랑 거리 3 이하만 움직임)
            - 도망자는 좌우 혹은 상하만 있음
            - 처음은 무조건 오른쪽, 아래쪽을 보고 시작
            - in : 술래 없으면 이동
            - out : 방향전환하고 술래 없으면 이동
        2. 술래
            달팽이대로 1칸씩 이동 -> 방향과 d를 미리 담아주기
    - 점수 : 턴 * 잡은 도망자 수
구상
    - 술래 이동/방향 배열 미리 만들어놓기 - 그냥 list로
    - 도망자들은 겹쳐질 수 있으므로 3차원 배열로
    - 나무위치는 2차원 배열로 따로담기
    1. run - 도망자 이동
        - run_possible() 거리 3 이하인 애들만
    2. police - 술래 이동
        view - 술래 잡기
    0   1  2  3
    좌 상  우  하
입력
    맵 n, 도망자 수 m, 나무 수 h, 턴 수 k
    도망자 위치 x,y,d (1: 좌우, 2: 상하) -> 1씩 빼주기
    나무 위치

5 1 1 60
2 4 1
2 4

'''

# 코드리팩토링: 달팽이 로직 1개만, 분기 간단히
def myprint(grid):
    print("-------------")
    for i in range(n):
        for j in range(n):
            print("↑→↓←"[grid[i][j]], end=" ")
        print()
def make_snape():
    r, c, d = n // 2, n // 2, 0
    num, two, cnt = 1, 0, 0
    while not (r == 0 and c == 0):
        center_zero[r][c] = d  # 여기서 넣어주고
        r = r + s_row[d]
        c = c + s_col[d]
        nd = d
        cnt += 1
        if cnt == num:
            two += 1
            nd = (d + 1) % 4
            cnt = 0
        if two == 2:
            num += 1
            two = 0
        zero_center[r][c] = (d + 2) % 4 # 바뀔 위치에서 전의 방향 거꾸로 넣어주기
        d = nd

    center_zero[0][0] = 2

def in_three(pr, pc):
    if abs(r - pr) + abs(c - pc) <= 3:
        return True
    return False


def run():  # 도망자 이동
    global grid
    new_grid = [[[] for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                for player_d in grid[i][j]:
                    if in_three(i, j):
                        nr = i + row[player_d]
                        nc = j + col[player_d]
                        if 0 <= nr < n and 0 <= nc < n:
                            if (nr, nc) != (r, c):
                                new_grid[nr][nc].append(player_d)
                            else:
                                new_grid[i][j].append(player_d)
                        else:
                            player_d = (player_d + 2) % 4  # 방향 틀어줌은 무조건
                            nr = i + row[player_d]  # 재계산
                            nc = j + col[player_d]
                            if (nr, nc) != (r, c):
                                new_grid[nr][nc].append(player_d)
                            else:
                                new_grid[i][j].append(player_d)
                    else:
                        new_grid[i][j].append(player_d)
    grid = new_grid


n, runner_num, tree_num, turn_num = map(int, input().split())
tree_grid = [[0] * n for i in range(n)]
grid = [[[] for i in range(n)] for i in range(n)]
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
for rn in range(runner_num):
    r, c, d = map(lambda x: int(x) - 1, input().split())
    grid[r][c].append(d)
for tn in range(tree_num):
    r, c = map(lambda x: int(x) - 1, input().split())
    tree_grid[r][c] = 1

# 방향 2차원 배열 2개 만들어놓기
s_row = [-1, 0, 1, 0]
s_col = [0, 1, 0, -1]
center_zero = [[0] * n for i in range(n)]
zero_center = [[0] * n for i in range(n)]
make_snape()

r, c = n // 2, n // 2
score = 0
change = 0
for turn in range(1, turn_num + 1):  # 턴수마다 무슨 배열 쓸껀지 계산 필요.
    if change == 0:
        dir_grid = center_zero
    else:
        dir_grid = zero_center
    catch = 0
    # 1. run - 도망자 이동
    run()
    # 2. police - 술래 이동
    d = dir_grid[r][c]
    nr = r + s_row[d]
    nc = c + s_col[d]
    # 2- 1. view - 술래 잡기
    view_d = dir_grid[nr][nc]
    for dist in range(0, 3):
        view_r = nr + s_row[view_d] * dist
        view_c = nc + s_col[view_d] * dist
        if 0 <= view_r < n and 0 <= view_c < n:
            if not tree_grid[view_r][view_c] and grid[view_r][view_c]:
                catch += len(grid[view_r][view_c])
                grid[view_r][view_c] = []

    score += (turn) * catch
    r = nr
    c = nc
    if r == 0 and c == 0: # 달팽이 바꿔야하나?
        change = 1
    elif r == n // 2 and c == n // 2:
        change = 0

print(score)
