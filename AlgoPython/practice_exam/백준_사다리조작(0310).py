'''
# 코드트리 디버깅
2025.03.29.토
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 2회
    문제 시작 21:29
    문제 종료 21:55

    총 풀이시간 26분
        29~34   : 문제 이해, 손코딩(5)
        34~38   : 2차원 배열 만들기(4)
        38~45   : combi(7)
        45~54   : 고객이 본인 번호와 연결되는지 확인 while 문(9)
                    와리가리 해서 left True 면 오른쪽은 못가게함
        54~55   : 틀린 테테 보니까 답이 0임...(1)
                    아 답이 0일수도 있구나 ㅠㅠ 수정!


  메모리 18 MB
  시간 66 ms

  회고
    1. 틀린이유: 답이 0이 되는 경우 고려 못함 으휴

'''

m, origin_num, n = map(int, input().split())
m = 2 * m - 1
grid = [[0] * (m) for i in range(n)]

for i in range(n):
    for j in range(0, m, 2):
        grid[i][j] = 1

for o in range(origin_num):
    r, c = map(int, input().split())
    grid[r - 1][2 * c - 1] = 1
arr = []
for i in range(n):
    for j in range(m):
        if not grid[i][j]:
            arr.append((i, j))


find = False


def is_ok():
    for j in range(0, m, 2):
        r, c = 0, j
        while r < n:
            left = False
            while c > 0 and grid[r][c - 1]:
                left = True
                c -= 1
            while not left and c < m - 1 and grid[r][c + 1]:
                c += 1
            r += 1
        if c != j:
            return False
    return True


def combi(sidx, idx):
    global find, grid
    if find:
        return
    if sidx == i:
        grid_origin = [_[:] for _ in grid]
        for r, c in sel:
            grid[r][c] = 1

        if is_ok():
            find = True
            return

        grid = [_[:] for _ in grid_origin]
        return
    if idx == len(arr):
        return

    if sidx > 0:
        nr, nc = arr[idx]  # 내가 선택할 것
        r, c = sel[sidx - 1]  # 내가 전에 선택한 것.
        if (r == nr) and (nc - c) == 2:  # 가로 연결되면 다음 거
            combi(sidx, idx + 1)
            return

    sel[sidx] = arr[idx]
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


ans = -1
for i in range(0, 4):
    sel = [0] * i
    combi(0, 0)
    if find:
        ans = i
        break
print(ans)


'''
# 백준 15684 사다리조작
# 체감난이도 골3 - 사다리를 어떻게 구현할지 아이디어 구상이 어려웠음.ㅜㅜ
# 김혜준 지켜야할 거 리스트업

    1. 문제 천천히.꼼꼼히 제발
    2. 2차원 배열 만들 때 for in range(n) 안붙힘
    3. 극간값 생각하기 예를 들어 100초까지면 99초까지봤음
    4. 작성시 한줄한줄 꼼꼼히 와라라락 쓰면 안됨. = 제발 차분히
    5. 보기랑 테케랑 다를 수 있으니 명심 파이어스톰에서 회전됐는데 보기랑 테케 달라서 계속 틀린줄 암
    6. 시뮬레이션에서 테케가 몇개 틀리면, 혹시 동작 순서가 이상한 건 아닌지 확인 (주사위 굴리기나 선물이 넘쳐흘러처럼)
    7. 인구이동 자료구조 만드는 거는 참고해도 될 듯 최적화 관련해서
    8. 프린트 안지우고 제출한거 2트임 진짜 왜구래ㅠ 확인하고 내야지
    9. 내가 관리해야할 대상이 여러개면 하나만 보지말고 대상 모두 전반적으로 print 해서 상태 확인하기
    10. 파핑파핑이나 다리만들기 bfs에서 미리 visited 초기화 해줘야함. r,c  하고 다음에 visited 처리하면 안됨.. nr,nc 에서 꼭 처리해줘야함
            -> 그래야 중복으로 안들어감
    11. 규칙찾기 진짜 못하는듯.. 그래도 찾아라 규칙 못찾으면 몸이 힘들다(드래곤 커브와 뱀을 기억해.......)

# 문제 풀고 나서 기록

    문제 시작 09:04(화장실 이슈)
    문제 종료 10:00
    총 풀이시간 56분
        04~07   : 문제 이해(3)
        08~21   : 문제 구상 및 초기 주석(13)
                    -> 여기서 좀 오래걸렸음(13) -> 근데 잘 한듯.!!! 덕분에 삽질방지
        21~30   :입력 받은 초기 사다리 만들기(9)
                    -> 여기서 잘 만들고 가야 실수가 없을 것 같아서 꼼꼼히 확인
        21~43   : 조합 함수 설계(22)
                    처음엔 가로 2개 연결되는 사다리를 안만들게끔 조합 코드 짜고싶었는데
                    뭔가 엣지케이스가 나올 것 같고.. 확신이 없어서
                    통조합 만들고 if sidx == m 도달한다음에 검증하는걸로 수정함
                    (제출 성공 후 수정해서 처음 계획대로 코드 짜보니까 100ms 정도 줄어들음)
        43~56   : j ==j 조건 만족하는 지 확인하는 함수 설계(13)
                    오른쪽으로만 쭉 가야하는데 오른쪽으로 갔다가 왼쪽가서 while 사용해서 수정
                    ctrl A+ delete 했는데 잘 했다.
        56~59   : 테케 나오는 거 확인, find True 됐을 때 나오는 사다리가 예시에 나오는 사다리랑 일치하는지 확인(3)
        59~00   : 오타 없는지 확인 (1)
                    -> 발견 ! 유레카
                    -> nr -> nr2로 수정

    메모리 151492 KB
    시간 3572 ms

    회고
    1. 아이디어 생각할 '꼭 2차원배열로 해야되나?', 'bfs 문제들처럼 노드 연결을 확인해야하나? 생각이 들었음'
    예시 사다리를 2차원 배열처럼 그려놔서 '2차원 배열이 맞다.' 라고 생각함 덕분에 삽질 방지

    2. 사다리를 어떻게 구현할 것인지 아이디어 내는게 어려웠음 문제에 2차원 배열로 그려놨길래 아이디어 획득

    3. 교수님 코드 이해하기!! -> j == j  확인하는거 다른 코드 보고 공부하기

    4. 화장실 갔다오고 풀어서 그런가 돌아와서 맘이 편했음..........
        그래서 아이디어 구상 시간도 차분히 천천히 한 것 같다.
        앞으로도 초반에 마음 진정좀 시키고 문제 읽자

    5. 시간복잡도 계산하고 들어간거 잘한듯!!!! 조합 시간복잡도가 4455100 나오길래 오케이 일단 해보자했음

# 문제 풀면서의 기록
문제 설명
    사다리 정보가 주어졌을 때
    모든 i 번이 i번으로 갈 수 있게끔
    최소한의 가로 사다리를 놓아라

입력
    세로선 갯수(열), 가로선 갯수, 가로선을 놓을 수 있는 H(행)
    기존에 있는 가로선
        a, b(a와 a+1 세로선에 가로 b번째 위치)

구상
    연결된 가로가 있으면 무조건 가고
    없으면 세로로감
    조합 인데 행 위치를 담아줘야 두개 이상 연결이 안된다

시간복잡도
    300개중에 최대 3개 고를 수 있음(조합)
    print((300*299*298)//(3*2)) = 4455100
    여기다 가로길이만큼 탐색하므로  4455100 * 30 * 10 = 1_336_530_000 = 13초인데
    하나라도 찾으면 튀게만들어서.. 괜찮을까 싶었다

넣어본 테케
    10 5 30
    1 1
    3 2
    2 3
    5 1
    5 4

'''

#################################################################
# 두번째 풀이 -> 가로 연결 2개 되는 애들은 애초에 안담음
# 첫번째 풀이와 100ms 시간차이
def isOk():
    for j in range(0, m, 2):
        r, c = 0, j
        while True:
            # 만약 다 내려왔는데 c가 j 가 아니면 return False
            if r == n:
                if c != j:
                    return False
                else:
                    break  # 맞다면 다음 j 탐색
            # 오른쪽이나 왼쪽에 사다리 있으면 무조건 간다.
            nr = r + row[0]
            nc = c + col[0]
            nr2 = r + row[1]
            nc2 = c + col[1]
            if 0 <= nc < m and grid[nr][nc] == 1:
                while 0 <= nc < m and grid[nr][nc] == 1:
                    r = nr
                    c = nc
                    nr = r + row[0]
                    nc = c + col[0]
                r += 1
            elif 0 <= nc2 < m and grid[nr2][nc2] == 1:
                while 0 <= nc2 < m and grid[nr2][nc2] == 1:
                    r = nr2
                    c = nc2
                    nr2 = r + row[1]
                    nc2 = c + col[1]
                r += 1
            else:
                # 아니면 내려만 간다.
                r += 1
    return True  # 여기까지 왔으면 조건 만족했음


def combi(sidx, idx, M):
    global find
    if find:
        return
    if sidx == M:
        for r, c in sel:
            grid[r][c] = 1
        if isOk():
            find = True
            return
        for r, c in sel:  # 원상복구
            grid[r][c] = 0
        return

    if idx == len(arr):
        return

    # 가로사다리 2개 연결되는지 검증
    if sidx > 0:
        pr, pc = sel[sidx - 1]  # 이전에 선택한 좌표
        r, c = arr[idx]  # 내가 선택하려는 좌표
        if pr == r and c - pc == 2:
            combi(sidx, idx + 1, M)  # 가로 2개네 ? 다음꺼 골라
            return

    sel[sidx] = arr[idx]
    combi(sidx + 1, idx + 1, M)
    combi(sidx, idx + 1, M)


m, origin_num, n = map(int, input().split())
m = m * 2 - 1
n = n + 1
grid = [[0] * (m) for i in range(n)]

# 짝수번째가 세로 사다리, 홀수번째가 가로 사다리가 될 것임
for j in range(0, m, 2):
    for i in range(n):
        grid[i][j] = 1

# 기존 가로 사다리 남겨주기
for i in range(origin_num):
    a, b = map(lambda x: int(x) - 1, input().split())  # a가 행
    grid[a][2 * b + 1] = 1

# 0인 곳은 모두 후보가 될 수 있음.
arr = []
for i in range(n - 1):
    for j in range(m):
        if grid[i][j] == 0:
            arr.append((i, j))
row = [0, 0]
col = [-1, 1]
ans = -1
find = False
for i in range(0, 4):
    sel = [0] * i  # 후보 선택
    combi(0, 0, i)
    if find:
        ans = i
        break
print(ans)
#################################################################
# 첫번째 풀이 -> 가로 연결 2개 되는 애들도 일단 담고 sidx == M 와서 검증
'''
문제 설명
    사다리 정보가 주어졌을 때
    모든 i 번이 i번으로 갈 수 있게끔
    최소한의 가로 사다리를 놓아라
입력
    세로선 갯수(열), 가로선 갯수, 가로선을 놓을 수 있는 H(행)
    기존에 있는 가로선
        a, b(a와 a+1 세로선에 가로 b번째 위치)
구상
    연결된 가로가 있으면 무조건 가고
    없으면 세로로감
    btk 인데 행 위치를 담아줘야 두개 이상 연결이 안된다
'''
m, origin_num, n = map(int, input().split())
m = m * 2 - 1
n = n + 1
grid = [[0] * (m) for i in range(n)]
# 짝수번째가 세로 사다리, 홀수번째가 가로 사다리가 될 것임
for j in range(m):
    for i in range(n):
        if j % 2 == 0:
            grid[i][j] = 1
# for _ in grid:
#     print(_)

for i in range(origin_num):
    a, b = map(lambda x: int(x) - 1, input().split())  # a가 행
    grid[a][2 * b + 1] = 1
# for _ in grid:
#     print(_)

# 0인 곳은 모두 후보가 될 수 있음.
arr = []
for i in range(n - 1):
    for j in range(m):
        if grid[i][j] == 0:
            arr.append((i, j))
row = [0, 0]
col = [-1, 1]


def isOk():
    # print("-------------------")
    # for _ in grid:
    #     print(_)
    for j in range(0, m, 2):
        r, c = 0, j
        while True:
            # 만약 다 내려왔는데 c가 j 가 아니면 return False
            if r == n:
                if c != j:
                    return False
                else:
                    break
            # 오른쪽이나 왼쪽에 사다리 있으면 무조건 간다.
            nr = r + row[0]
            nc = c + col[0]
            nr2 = r + row[1]
            nc2 = c + col[1]
            if 0 <= nc < m and grid[nr][nc] == 1:
                while 0 <= nc < m and grid[nr][nc] == 1:
                    r = nr
                    c = nc
                    nr = r + row[0]
                    nc = c + col[0]
                r += 1
            elif 0 <= nc2 < m and grid[nr2][nc2] == 1:
                while 0 <= nc2 < m and grid[nr2][nc2] == 1:
                    r = nr2
                    c = nc2
                    nr2 = r + row[1]
                    nc2 = c + col[1]
                r += 1
            else:
                # 아니면 내려만 간다.
                r += 1
    # for _ in grid:
    #     print(_)
    return True


def combi(sidx, idx, M):
    global find
    if find:
        return
    if sidx == M:
        # 검증
        for i in range(M - 1):
            r, c = sel[i]
            nr, nc = sel[i + 1]
            if r == nr and nc - c == 2:
                return
        for r, c in sel:
            grid[r][c] = 1
        if isOk():
            find = True
            return
        for r, c in sel:  # 원상복구
            grid[r][c] = 0

        return
    if idx == len(arr):
        return

    sel[sidx] = arr[idx]
    combi(sidx + 1, idx + 1, M)
    combi(sidx, idx + 1, M)


ans = -1
find = False
for i in range(0, 4):
    sel = [0] * i  # 후보 선택
    combi(0, 0, i)
    if find:
        ans = i
        break
print(ans)
