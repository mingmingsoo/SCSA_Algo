'''
# 코드트리 돌아가는 팔각의자
2025.03.29.토
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 20:07
    문제 종료

    총 풀이시간 20분
        07~12   : 문제 이해, 초기 주석(3)
        34~39   : combi 설계(5)
        39~45   : 절반만 돌게 (n)C(n//2) 계산 -> 사실 sel[0] != 0 return 과 같은 것.(6)
        45~51   : 이중 포문 돌게해서 점수 계산 설계(6)

  메모리 23 MB
  시간 324 ms

# 문제 풀면서의 기록
시간복잡도
명령수 50* 회전횟수 m 50* 인접찾기 n,m 50*50
50^4
'''
from collections import deque

n, m, order_num = map(int, input().split())
grid = [deque(map(int, input().split())) for i in range(n)]

for order in range(order_num):
    x, d, ro = map(int, input().split())
    if d == 0:
        d = 1
    else:
        d = -1
    ro *= d

    for i in range(x - 1, n, x):  # 배수만..
        grid[i].rotate(ro)


    # 인접 찾기
    is_close = False
    close = [[0] * m for i in range(n)]
    # 가로 찾자
    for i in range(n):
        for j in range(-1, m - 1, 1):
            if grid[i][j] and grid[i][j] == grid[i][j + 1]:
                close[i][j] = close[i][j + 1] = 1
                is_close = True
    # 세로 찾자
    for j in range(m):
        for i in range(n - 1):
            if grid[i][j] and grid[i][j] == grid[i + 1][j]:
                close[i][j] = close[i + 1][j] = 1
                is_close = True

    if is_close:
        for i in range(n):
            for j in range(m):
                if close[i][j]:
                    grid[i][j] = 0
    else:
        cnt = 0
        sm = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    cnt += 1
                    sm += grid[i][j]

        for i in range(n):
            for j in range(m):
                if grid[i][j] and grid[i][j] > sm // cnt:
                    grid[i][j] -= 1
                elif grid[i][j] and grid[i][j] < sm // cnt:
                    grid[i][j] += 1

print(sum(map(sum, grid)))


'''
# 백준 17822 원판돌리기
# 체감난이도 골4

# 문제 풀고 나서 기록

    문제 시작 09:00
    문제 종료 09:48
    총 풀이시간 48분
        00~09   : 문제 이해(9)
                    처음엔 2차원 배열처럼 생각해서 m이 어떻게 6이될 수 있는지 이해가 잘 안됐음
                    2차원 배열로 숫자 넣어서 회전시킬까? 했는데 그게 아니라 그냥 rotation 시키면 된다고 생각함.
                    일단 m이 4일때를 고려해서 풀기시작.
        09~12   : 문제 구상 및 초기 주석(3)
                    deque rotation 쓰면 편하겠다고 생각했지만 조회도 해야하기에 deque이 조회가 되나?
                    조회 안되면 list로 바꾸자 라고 생각
        12~15   : 2차원 배열에 deque 넣었는데 역시나 조회 안됨! list로 변경(3)
        21~23   : 회전 로직 설계(2)
                    슬라이싱 할까 했지만 append, pop도 괜찮다고 생각했음
                    -> k 가 클 수 도 있기에 append, pop 할거면 나머지 연산자로 해야된다고 생각
        23~27 : 인접한 애들 찾는 로직 설계(4)
                한번에 0으로 바꾸려고 delete 배열과 is_delete flag 만듬
                for i 를 (-1, m-1) 로 해서 1과 M번째가 인접한지 확인해줬음
        27~30 : 평균 구하는 로직 설계(3)
        30~35 : 오픈테케 답 안나오는 거 확인, 디버깅 시작(5)
                인접한 애들 찾는 로직에서 0인 애들도 인접하다는 코드여서 != 0 조건문 추가
                더해주고 빼주는 로직에서도 0인애들 영향받아서 !=0 조건문 추가
        35~38 : m이 4일땐 잘 나오는데 m이 6일때 테케가 잘 안 나오는 거 확인(3) <- (당연한 결과)
                6일때 그려보니 규칙이 보여서 k = k%4 에서 k = k%m으로 수정
        38~46 : 아뿔싸 그래도 m이 6일때 답이 안나옴(8)
                문제 조건이 작거나 클 때 인데 나는 if 클때 else: 여서
                평균하고 같을 때도 연산이 들어간거 확인! 조건문 수정
        46~48 : 내 테케 검증(2)
                n,m 최솟값일 때

    메모리 115496 KB
    시간 168 ms

    회고
    1. 여러모로 오픈테케 의존 많이했다................ m이 4가 아닌 테케가 없었으면 아찔했음 ㅠㅠ
        '처음부터 조건문을 잘 짰으면 좋았을텐데' 하는 아쉬움이 있음...
        ★ 조건 확인 잘하기!
    2. 잘한점은 문제이해와 구상을 확실히 하고 넘어간거 ! 까딱했으면 2차원 배열에 숫자 남겨서 풀뻔
    2. deque에 list로 넣으면 조회되는거 친구들 코드 보고 확인... 수정해보기!
    3. append, pop 말고 슬라이싱 방법도 이해하기!

# 문제 풀면서의 기록
문제설명
    원판을 회전시켜라.
    원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
    그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
    없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
입력
    원판 갯수 N, 원판에 몇개들었는지 M, 명령 수
    원판 정보
    명령 정보
        x,d,k :x의 배수인 원판을 d방향으로 k번 회전 (0 시계, 1 반시계)
        k는 M보다 작음.
구상
    회전: 1 2 3 4 5 6
         1 2 3 0 1 2 ...
    회전은 m의 나머지
테케
    2 2 1
    1 2
    3 4
    1 0 1
'''

n, m, order_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
for o in range(order_num):
    x, d, k = map(int, input().split())
    k = k % m
    # 회전
    for i in range(x - 1, n, x):  # x 의 배수인 애들 회전
        arr = grid[i][:]
        if d == 0:
            for kk in range(k):
                arr.insert(0, arr.pop())
        elif d == 1:
            for kk in range(k):
                arr.append(arr.pop(0))
        grid[i] = arr
    # 회전 끝

    is_delete = False
    delete = [[0] * m for i in range(n)]
    # 1. 같은 원 확인
    for i in range(n):
        for j in range(-1, m - 1):  # 0하고 m-1은 연결된다.
            if grid[i][j] != 0:
                if grid[i][j] == grid[i][j + 1]:
                    delete[i][j], delete[i][j + 1] = 1, 1
                    is_delete = True

    # 2. 세로 확인
    for j in range(m):
        for i in range(n - 1):
            if grid[i][j] != 0:
                if grid[i][j] == grid[i + 1][j]:
                    delete[i][j], delete[i + 1][j] = 1, 1
                    is_delete = True

    # 삭제가능하면 삭제
    if is_delete:
        for i in range(n):
            for j in range(m):
                if delete[i][j] == 1:
                    grid[i][j] = 0
    # 아니라면 평균 구하기
    else:
        cnt = sm = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    cnt += 1
                    sm += grid[i][j]

        for i in range(n):
            for j in range(m):
                if grid[i][j] <= 0:
                    continue
                if grid[i][j] < (sm / cnt): grid[i][j] += 1
                elif grid[i][j] > (sm / cnt): grid[i][j] -= 1

ans = sum(map(sum, grid))
print(ans)
