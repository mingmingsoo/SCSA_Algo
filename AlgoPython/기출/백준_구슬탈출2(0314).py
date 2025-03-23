'''
# 13460 백준 구슬탈출2
# 체감난이도 골2

# 문제 풀고 나서 기록

    문제 시작 09:00
    문제 종료 10:04
    총 풀이시간 64분
        00~02   : 문제 이해(2)
        02~05   : 초기 주석 및 문제 구상(3)
        05~50   : 1차 설계(45)
                    몇 테케는 나왔으나 구슬이 겹칠 때 로직이 잘 되지 않는 것 확인...
                    빨간볼 파란볼 한번에 관리하고 싶었으나 겹칠 때 처리가 잘 안돼서
                    (1) 빨간볼 움직임
                    (2) 파란볼 움직임
                    (3) 겹치는지 검사해서 k 에따라 +1, -1조정으로 계획 수정
        50~00   : 2차 설계 완료(10)
        00~04   : (1)마지막 테케에서 겹쳐지는 거 잘 처리되는지 확인
                  (2) O에 둘 다 들어갈 때 continue 되는 거 확인
                    제출완료


    메모리 127392 KB
    시간 232 ms

    회고
        1. 프린트 안지우고 낸거 진짜 넌 대단하다 대단해
        2. 변수명을 잘쓰자............ 코드짜면서도 헷갈렸음


# 문제 풀면서의 기록
문제설명
    동서남북으로 기울여서 빨간구슬 빼기
    1. 파란 구슬이 먼저 빠지면 실패
    2. 빨간 구슬과 파란 구슬이 동시에 빠져도 실패
    3. 10번까지만 가능

구상
    while로 동서남북을 보내고 가다가 O를 만나는지 검사한다.
    1. 이때 빨간것도 O고 파란것도 O면 continue
    2. 이때 빨간건 아닌데 파란거가 O면 continue
    3. 중복 위치를 검사하는게 어려운데
        보내면서 다른 공의 위치를 각자 검사해준다.
    visited는 쓰지 않겠다.
'''
#########################################################
# 첫번째 풀이
from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
rr = rc = br = bc = -1
er, ec = -1, -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == "R":
            rr = i
            rc = j
            grid[i][j] = "."
        elif grid[i][j] == "B":
            br = i
            bc = j
            grid[i][j] = "."
        elif grid[i][j] == "O":
            er = i
            ec = j
            grid[i][j] = "."

q = deque([(rr, rc, br, bc, 0)])
ans = -1
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def game():
    global ans
    while q:
        rr, rc, br, bc, cnt = q.popleft()
        if cnt > 10:
            return
        if (rr == er and rc == ec) and not (br == er and bc == ec):
            ans = cnt
            return
        if (rr == er and rc == ec) and (br == er and bc == ec):
            continue
        if br == er and bc == ec:  # 파란거 먼저 왔으면 다음꺼 탐색.
            continue
        # print("red: ", (rr, rc), "blue: ", (br, bc))
        orr, orc, obr, obc = rr, rc, br, bc
        for k in range(4):
            rr, rc, br, bc = orr, orc, obr, obc
            while True:
                nrr = rr + row[k]
                nrc = rc + col[k]
                # 빨강이 검사.
                if 0 <= nrr < n and 0 <= nrc < m and grid[nrr][nrc] == ".":  #
                    rr = nrr
                    rc = nrc
                    if rr == er and rc == ec:
                        break
                else:
                    break
            while True:
                nbr = br + row[k]
                nbc = bc + col[k]
                # 파랑이 검사.
                if 0 <= nbr < n and 0 <= nbc < m and grid[nbr][nbc] == ".":  #
                    br = nbr
                    bc = nbc
                    if br == er and bc == ec:
                        break
                else:
                    break
            # 중복되는 위치 검사.
            if rr == br and rc == bc and not (rr == er and rc == ec):
                if k == 0:  # 북쪽으로 갔음
                    if obr > orr:
                        br += 1
                    else:
                        rr += 1
                elif k == 1:  # 남쪽으로 갔음
                    if obr < orr:
                        br -= 1
                    else:
                        rr -= 1
                elif k == 2:  # 오른쪽으로 갔음
                    if obc < orc:  # 파란색이 왼쪽에 있었으면
                        bc -= 1
                    else:
                        rc -= 1
                elif k == 3:  # 왼쪽으로 갔음
                    if obc > orc:  # 파란색이 오른쪽에 있었으면
                        bc += 1
                    else:
                        rc += 1

            if not (rr == orr and rc == orc and br == obr and bc == obc):
                q.append((rr, rc, br, bc, cnt + 1))


game()
print(ans)

#########################################################
# 3번째 풀이 함수화
from collections import deque


def move(r, c, k):
    while True:
        nr = r + row[k]
        nc = c + col[k]
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "#":
            r = nr
            c = nc
            if grid[r][c] == "O":
                break
        else:
            break
    return r, c


def game():
    global ans
    while q:
        red_r, red_c, blue_r, blue_c, cnt = q.popleft()
        if cnt > 10:
            return
        if grid[blue_r][blue_c] == "O":  # 파란거 왔으면 동시에 왔든, 파랑이만 왔든 다음꺼 탐색.
            continue
        if grid[red_r][red_c] == "O":
            ans = cnt
            return

        for k in range(4):
            # 빨강이 움직여
            next_red_r, next_red_c = move(red_r, red_c, k)
            # 파랑이 움직여
            next_blue_r, next_blue_c = move(blue_r, blue_c, k)

            # 중복되는 위치 검사.
            if next_red_r == next_blue_r and next_red_c == next_blue_c and not grid[next_red_r][
                                                                                   next_red_c] == "O":  # 목적지말고
                if k == 0:  # 북쪽으로 갔음
                    if blue_r > red_r:
                        next_blue_r += 1
                    else:
                        next_red_r += 1
                elif k == 1:  # 남쪽으로 갔음
                    if blue_r < red_r:
                        next_blue_r -= 1
                    else:
                        next_red_r -= 1
                elif k == 2:  # 오른쪽으로 갔음
                    if blue_c < red_c:  # 파란색이 왼쪽에 있었으면
                        next_blue_c -= 1
                    else:
                        next_red_c -= 1
                elif k == 3:  # 왼쪽으로 갔음
                    if blue_c > red_c:  # 파란색이 오른쪽에 있었으면
                        next_blue_c += 1
                    else:
                        next_red_c += 1
            # 빨, 파 둘 다 가만히 있었으면 q에 안넣어줌
            if not (
                    red_r == next_red_r and red_c == next_red_c and blue_r == next_blue_r and blue_c == next_blue_c):
                q.append((next_red_r, next_red_c, next_blue_r, next_blue_c, cnt + 1))


n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
red_r = red_c = blue_r = blue_c = -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == "R":
            red_r, red_c = i, j
            grid[i][j] = "."
        elif grid[i][j] == "B":
            blue_r, blue_c = i, j
            grid[i][j] = "."

q = deque([(red_r, red_c, blue_r, blue_c, 0)])
ans = -1
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

game()
print(ans)

