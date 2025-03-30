'''
# 코드트리 이상한체스(백준 감시)
2025.03.29.토
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 20:43
    문제 종료 08:41

    총 풀이시간 9분

  메모리 24 MB
  시간 1485 ms

# 문제 풀면서의 기록
시간복잡도
턴수 1000 * 말 수 10
ㄱㅊ
'''
n, horse_num = map(int, input().split())
grid = [[2] * (n + 2)] + [[2] + list(map(int, input().split())) + [2] for i in range(n)] + [[2] * (n + 2)]
n += 2
horse_grid = [[[] for i in range(n)] for i in range(n)]
horse_list = [0]
for h in range(1, horse_num + 1):
    r, c, d = map(int, input().split())
    horse_grid[r][c].append(h)
    horse_list.append([r, c, d - 1])
ans = -1
row = [0, 0, -1, 1]
col = [1, -1, 0, 0]
change_dir = [1, 0, 3, 2]
end = False
for time in range(1, 1001):
    for idx, horse in enumerate(horse_list):
        if idx == 0:
            continue
        r, c, d = horse
        nr = r + row[d]
        nc = c + col[d]
        if grid[nr][nc] == 2:
            d = change_dir[d]
            horse_list[idx][2] = d
        # 재계산
        r, c, d = horse
        nr = r + row[d]
        nc = c + col[d]
        if grid[nr][nc] == 2:
            continue  # 그래도 파란색이면 넘어가.

        # 나랑 같이 이동해야되는 내 위에 애들...
        move_lst = []
        for w in range(len(horse_grid[r][c])):
            if horse_grid[r][c][w] == idx:
                move_lst = horse_grid[r][c][w:]
                horse_grid[r][c] = horse_grid[r][c][:w]
                break
        if grid[nr][nc] == 1:
            move_lst.reverse()  # 반대!
        horse_grid[nr][nc].extend(move_lst)
        if len(horse_grid[nr][nc]) >= 4:
            end = True
            ans = time
            break
        for midx in move_lst:
            horse_list[midx][0] = nr
            horse_list[midx][1] = nc

    if end:
        break
print(ans)


'''

# 17837 백준 새로운 게임2
# 체감난이도 골2

# 문제 풀고 나서 기록

    문제 시작 09:00
    문제 종료 11:32
    총 풀이시간 152분
        00~04   : 문제 이해(4)
        04~16   : 문제 구상 및 초기 주석(12)
                    2차원 배열을 말 순서대로 탐색하는게 비효율적인 것 같아서
                    2차원 배열엔 말넘버만 담고 말들은 1차원 배열에 관리해야겠다고 생각.
        12~35   : 위 구상처럼 초기 설계하다가(23)
                    말이 합쳐질 때 1차원 배열에서 말들 좌표를 다 바꾸는게 더 어려울 것 같아서
                    1차원 배열 없이 말 순서대로 이차원배열을 탐색하는 걸로 계획 변경
        35~03   : 1차 설계(28)
                1차 디버깅
                말 발견하면 break 해야하는데
                for 문이 많다보니 flag 위치가 안맞아서 말 순서가 안 넘어가서 디버깅 했음
                그러니까 함수화하지 이자식아.
        03~37   : 5번 예제 out of range 떠서 디버깅 시작...(34)
                파란칸으로 갈때랑 범위 넘어갈때 방향바꾸는 게 틀린 것 같아서 수정
                다솔관 문제도 그랬는데 이런거 진짜  약한듯 ㅠㅠ
        37~32   : 그래도 예제 5번 답이 안나와서 디버깅(55)
                울고싶었음 내 로직이 틀린게 없어보였는데... (위에 디버깅했던건 의심스럽긴했음)
                7일 때 4개 합쳐지는것도 봤음
                근데 턴 끝나고 4개 검사하는건줄 암. 니잘못이지 뭐

    메모리 113188 KB
    시간 188 ms

    회고
        1. 디버깅 오래한 이유:
        종료조건이 턴 끝나고 검사인줄 알았는데 4개가 발견되면 바로 종료인걸 몰랐다.
        .........................
        이것만 디버깅 엄청 오래한듯.............속상하다
        그래도 풀었으니 됐다.
        조건검사 확실히하고..................
        입출력 정리 잘하라고 그니까!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# 문제 풀면서의 기록
문제 설명
    1번말부터 K번말까지 순서대로 이동시킨다.
    한 말이 이동할 때 올려져있는 말도 함께 이동(?)
    말이 4개이상 쌓이면 게임 종료(k개 아님)
    1. A번말이 흰색이로 이동하려는 경우
        말이 있을 때 A는 위에 올라감
        A번 위에 다른 말이 있을 때는 A번위에 모든 말이 이동
        C           C
        B  E        B
        A  D   ->   A
                    E
                    D
    2. 빨간색으로 이동하는 경우, A번말 은 순서가 바뀜
        ABC -> CBA
        G           A
        F  E        D
        D  C   ->   F
        A  B        G
                    B
                    C
                    E
    3. 파란색인 경우 이동방향 반대
        만약 반대에도 파란색이 있으면 유지.

헷갈렸던 점
    213 이런식으로 있으면 1번말이면 1~부터 이동 2는 안간다.
    범위를 벗어나면 d가 반대로? 아아 ㅇㅇ 그렇대
구상
    append 할지 insert 할지
입력
    맵크기, 말갯수
    체스판 정보(0흰 1빨 2파)
    말 정보 1부터
출력
    게임 종료되는 턴
    1000보다 크면 -1 출력
    같은 칸에 말이 두 개 이상 있는 경우는 입력으로 주어지지 않는다. -> 0 일 수 없다.

'''


class Horse:
    def __init__(self, num, d):
        self.num = num
        self.d = d


n, horse_num = map(int, input().split())
color = [list(map(int, input().split())) for i in range(n)]
grid = [[[] for i in range(n)] for i in range(n)]
for horse in range(horse_num):
    r, c, d = map(int, input().split())
    grid[r - 1][c - 1].append(Horse(horse + 1, d - 1))  # 넘버링, 방향

ans = -1

row = [0, 0, -1, 1]
col = [1, -1, 0, 0]
move = {0: 1, 1: 0, 2: 3, 3: 2}


def valid():
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) >= 4:
                return True
    return False


def is_range(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


for turn in range(1, 1001):
    real_find = False
    # move
    for order in range(1, horse_num + 1):
        find = False
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    for w in range(len(grid[r][c])):
                        horse = grid[r][c][w]
                        if horse.num == order:  # 움직임 수행
                            if not is_range(r + row[horse.d], c + col[horse.d]) \
                                    or color[r + row[horse.d]][c + col[horse.d]] == 2:
                                # 방향 전환 필요
                                horse.d = move[horse.d]
                            # 이동할 위치
                            nr = r + row[horse.d]
                            nc = c + col[horse.d]
                            # 흰색 검사
                            if is_range(nr, nc) and color[nr][nc] == 0:
                                # 내 위에 말들 모두 올린다
                                for k in range(w, len(grid[r][c])):
                                    grid[nr][nc].append(grid[r][c][k])
                                # 그리고 제거
                                for k in range(len(grid[r][c]) - 1, w - 1, -1):
                                    grid[r][c].pop(k)

                            # 빨간색 검사
                            elif is_range(nr, nc) and color[nr][nc] == 1:
                                # 내 위에 말들 뒤에서부터 올린다.
                                for k in range(len(grid[r][c]) - 1, w - 1, -1):
                                    grid[nr][nc].append(grid[r][c][k])
                                # 그리고 제거
                                for k in range(len(grid[r][c]) - 1, w - 1, -1):
                                    grid[r][c].pop(k)
                            find = True
                            break
                if find:
                    break
            if find:
                break
        # valid
        if valid():
            ans = turn
            real_find = True
            break
    if real_find:
        break
print(ans)


def myprint():
    print("--------------------------", turn, order)
    for i in range(n):
        for j in range(n):
            tmp = ""
            if grid[i][j]:
                for horse in grid[i][j]:
                    tmp += str(horse.num)
                    if horse.d == 0:
                        tmp += ">"
                    if horse.d == 1:
                        tmp += "<"
                    if horse.d == 2:
                        tmp += "^"
                    if horse.d == 3:
                        tmp += "v"
                print(tmp, end=" ")
            else:
                if color[i][j] == 0:
                    print("W", end=" ")
                if color[i][j] == 1:
                    print("R", end=" ")
                if color[i][j] == 2:
                    print("B", end=" ")
        print()
