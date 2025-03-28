'''
# 0322 2회차 풀이(3회차 안해도 될듯)
# 코드트리 2개의 사탕 (백준 구슬탈출2)
# 체감난이도 골2~골3

# 문제 풀고 나서 기록
    제출 횟수 1회
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
        메모리 19 MB
        시간 91 ms
    - visited 안쓰면
        메모리 16 MB
        시간 49 ms

    회고
        1. visited 로직도 추가하니까
            -> 시간 91ms에서 49ms로 줄어듬
        2. 구슬탈출 1~4까지 풀어서 3회차 풀이는 안해도 괜찮을 것 같다.
        3. 구슬 움직이는 로직을 함수화로 처음부터 하니까 코드짜기가 편했다! 설계를 합시다!
        4. 변수가 길어지니까 좀 불편해서... nrr, nrc 이렇게 쓰면 좀 더 좋을 듯??

# 문제 풀면서의 기록
문제설명
    상자를 상하좌우로 기울여서 빨간사탕을 빼내기
    1. 파란사탕이 나와선 안됨
    2. 동시에 나와서도 안됨
    3. 즉 빨간사탕만 나와야함
입력
    맵 정보
출력
    상자를 기울이는 최소 횟수
구상
    1. bfs로 상하좌우 움직인 것을 q에 넣어준다.
    2. 조건 검사를 파란사탕이 들어왔으면 continue 해서 그 답을 피해가게함
    3. 위치가 겹칠때 처리를 해줘야함.(누가 먼저 왔냐 따져주기)
    4. 최대 답은 10임
        즉 11이 되면 return 하기 -> 조건문 위치 중요
    5. #으로 막혀있어서 범위검사는 안해도 될듯
시간복잡도
    n * m * 4^10
    맵 크기 * 굴리는 경우의 수
    104,857,600 인데.... q에 그만큼 안넣는다
'''
from collections import deque


def move(origin_r, origin_c, k):
    r, c = origin_r, origin_c
    while True:
        nr = r + row[k]
        nc = c + col[k]

        if grid[nr][nc] == "#":
            break
        r = nr
        c = nc
        if (r, c) == (er, ec):
            break

    return r, c


def bfs(srr, src, sbr, sbc):
    global ans
    q = deque([(srr, src, sbr, sbc, 0)])
    visited = set([(srr, src, sbr, sbc)])
    while q:
        red_r, red_c, blue_r, blue_c, time = q.popleft()
        if time > 10:  # 게임 종료
            return
        if (blue_r, blue_c) == (er, ec):
            continue  # 파란공 들어왔으면 넘어가기
        if (red_r, red_c) == (er, ec):
            ans = time  # 빨간공만 들어왔으면 종료
            return

        for k in range(4):
            next_red_r, next_red_c = move(red_r, red_c, k)
            next_blue_r, next_blue_c = move(blue_r, blue_c, k)

            if (next_red_r, next_red_c) == (next_blue_r, next_blue_c) and (next_red_r, next_red_c) != (er, ec):
                # 공 빠질때말고 겹쳤을 때 처리 필요
                if k == 0:  # 상
                    if blue_r < red_r:
                        next_red_r += 1
                    else:
                        next_blue_r += 1
                elif k == 1:  # 하
                    if blue_r > red_r:
                        next_red_r -= 1
                    else:
                        next_blue_r -= 1
                elif k == 2:  # 좌
                    if blue_c < red_c:
                        next_red_c += 1
                    else:
                        next_blue_c += 1
                elif k == 3:  # 우
                    if blue_c > red_c:
                        next_red_c -= 1
                    else:
                        next_blue_c -= 1
            if (red_r, red_c) == (next_red_r, next_red_c) and (blue_r, blue_c) == (next_blue_r, next_blue_c):
                continue
            else:
                if (next_red_r, next_red_c, next_blue_r, next_blue_c) not in visited:
                    visited.add((next_red_r, next_red_c, next_blue_r, next_blue_c))
                    q.append((next_red_r, next_red_c, next_blue_r, next_blue_c, time + 1))


n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
red_r = red_c = blue_r = blue_c = er = ec = - 1
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if grid[i][j] == "R":
            red_r, red_c = i, j
            grid[i][j] = "."
        elif grid[i][j] == "B":
            blue_r, blue_c = i, j
            grid[i][j] = "."
        elif grid[i][j] == "O":
            er, ec = i, j
            grid[i][j] = "."

ans = -1

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

bfs(red_r, red_c, blue_r, blue_c)
print(ans)

'''
# 0314 1회차 풀이
# 13460 백준 구슬탈출2
# 체감난이도 골2

# 문제 풀고 나서 기록
    제출횟수 1회
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
