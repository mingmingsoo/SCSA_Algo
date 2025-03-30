'''
코드트리 바이러스 실험
'''


n, virus_num, time = map(int, input().split())
feed = [[5] * n for i in range(n)]
plus = [list(map(int, input().split())) for i in range(n)]  # 추가되는 양분
grid = [[[] for i in range(n)] for i in range(n)]
row = [-1, 1, 0, 0, 1, 1, -1, -1]
col = [0, 0, 1, -1, 1, -1, 1, -1]
for v in range(virus_num):
    r, c, age = map(int, input().split())
    grid[r - 1][c - 1].append(age)

for t in range(time):

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                grid[i][j].sort()  # 오름차순 해주고
                die_idx = len(grid[i][j])
                for idx, age in enumerate(grid[i][j]):
                    if age <= feed[i][j]:
                        feed[i][j] -= age
                        grid[i][j][idx] += 1
                    else:
                        die_idx = idx
                        break

                for idx in range(die_idx, len(grid[i][j])):
                    feed[i][j] += grid[i][j][idx] // 2

                grid[i][j] = grid[i][j][:die_idx]
    # print("----양분----")
    # for _ in grid:
    #     print(_)
    # 번식
    for i in range(n):
        for j in range(n):
            for idx, age in enumerate(grid[i][j]):
                if age % 5 == 0:
                    for k in range(8):
                        nr = i + row[k]
                        nc = j + col[k]
                        if not (0 <= nr < n and 0 <= nc < n):
                            continue
                        grid[nr][nc].append(1)
    # print("----번식----")
    # for _ in grid:
    #     print(_)
    # 양분 추가
    for i in range(n):
        for j in range(n):
            feed[i][j] += plus[i][j]
    # print("----양분추가----")
    # for _ in feed:
    #     print(_)
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(grid[i][j])
print(ans)



'''
# 백준 16235 나무 재테크
# 체감난이도 골5 인데 시간 제한 때문에 골3이 맞다.
# 시뮬레이션이라고 너무 동작 순서별로 기능 나누지 말고!!
    일단 기능 나눈 다음에 혹시 동작들을 합쳐도 되는지 확인하기!!!

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
    11. 규칙찾기 진짜 못하는듯.. 그래도 찾아라 규칙 못찾으면 몸이 힘들다
    12. 시뮬레이션이라고 너무 동작 순서별로 기능 나누지 말고!!
            일단 나눈 다음에 혹시 동작들을 합쳐도 되는지 확인하기!!!(나무재테크처럼)


# 문제 풀고 나서 기록

    문제 시작 13:40
    1차 제출 14:04 ※sort 안할거면 insert(0) 해야하는데 안해서 틀림※
    2차 제출 14:12 ※시간초과 -> 군더더기 다 빼야겠다고 생각.※
    문제 종료 14:35
    총 풀이시간 55분
        40~44   : 문제 이해(4)
        44~47   : 문제 구상 및 초기 주석(13)
        47~04   : 1차 제출 완료 및 틀렸습니다.(17)
                    문제에서 주어지는 봄/여름/가을/겨울 나눠서 코드를 짰음
        04~12   : 2차 제출 완료 및 시간초과.(8)
                    번식할 때 append이기에 sort를 안하면 틀리는 코드인 거 확인
        12~24   : 3차 제출 완료 및 시간초과(12)
                    죽은애들을 remove 하지 않고 pop으로 수정
                    죽은애들을 dies에 모아서 한번에 양분 주는걸로 수정
        24~35   : 4차 제출완료
                    생각해보니 class의 live 정보가 필요없다고 판단.
                    class 사용하지 않고 grid에 나이만 넣어줌
                    그리고 die_idx가 생기면 break 하고
                    die_idx부터 양분을 더해주고 pop을 바로바로 해줌
                    즉 봄과 여름 한번에 진행
                    그리고 어차피 1인 애들은 %5에 영향을 받지 않으므로
                    new_grid를 따로 생성하지않고 grid에 바로 넣어줌

    메모리 122352 KB
    시간 520 ms

    회고
    1. 시간복잡도 계산하는게 어려워서 일단 구현했다... 역시나 시간초과가 떴다.
    2. 이런 순서가 있는 시뮬에션 문제에선 순서대로 진행하면 대체적으로 맞았는데 시간초과가 나서 당황했다 ㅠㅠ
        시간초과가 나서 문제를 분석해보니 굳이 봄,여름,가을,겨울을 나누지 않아도 된다는 것을 확인했고 불필요한 작업을 제거해주었다.
        좋은 경험이라고 생각한다.
        굳이 구분하지 않아도 되는 작업은 구분하지 않는 것!!
        시간초과가 나기전에 한번 더 생각해보기!!!


# 문제 풀면서의 기록
문제설명
    N*N 크기에 나무가 심어져 있음.
    처음엔 모두 양분 5
    M개의 나무
    1. 봄에는 나이만큼 양분 먹고 나이 증가.
        만약 한 칸에 나무가 여러개면
        어린 나무부터 양분을 먹는다.
        양분 못먹으면 양분이 죽는다
    2. 여름에는 봄에 죽은 나무가 양분으로 변함
        죽은 나무 나이 // 2가 양분에 추가

    3. 가을에는 나무 번식.
        나이가 5의 배수일때만 가능
        인접8칸에 나이가 1인애들 생김
    4. 겨울엔 양분 추가.
구상
    class로 나무 관리. 속성: 나이,살았는지 죽었는지. -> 뺐음
    시뮬레이션임

10 10 1000
2 3 2 3 2 2 3 2 3 2
2 3 2 3 2 2 3 2 3 2
2 3 2 3 2 2 3 2 3 2
2 3 2 3 2 2 3 2 3 2
2 3 2 3 2 2 3 2 3 2
2 3 2 3 2 2 3 2 3 2
2 3 2 3 2 2 3 2 3 2
2 3 2 3 2 2 3 2 3 2
2 3 2 3 2 2 3 2 3 2
2 3 2 3 2 2 3 2 3 2
1 2 3
1 3 3
1 4 3
1 5 3
1 6 3
3 1 3
3 2 3
3 3 3
3 4 3
3 5 3

1 3 1
1
1 1 7
1 1 6
1 1 5

정답 1
'''

n, m, limit = map(int, input().split())
fill = [list(map(int, input().split())) for i in range(n)]
row = [0, 0, 1, -1, 1, 1, -1, -1]
col = [1, -1, 0, 0, 1, -1, 1, -1]
grid = [[[] for j in range(n)] for i in range(n)]
nutrition = [[5] * n for i in range(n)]
tmp = []
for mm in range(m):
    r, c, age = map(int, input().split())
    r -= 1
    c -= 1
    grid[r][c].append(age)  # 나이

for time in range(limit):

    # 나이순 정렬.
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                grid[i][j].sort()

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                die_idx = -1
                for w in range(len(grid[i][j])):
                    tree_age = grid[i][j][w]
                    if nutrition[i][j] >= tree_age:
                        nutrition[i][j] -= tree_age
                        grid[i][j][w] += 1
                    else:
                        die_idx = w
                        break
                # 죽은애들 없애주면서 양분 추가하기
                if die_idx != -1:
                    for w in range(len(grid[i][j]) - 1, die_idx - 1, -1):
                        nutrition[i][j] += grid[i][j][w] // 2
                        grid[i][j].pop(w)

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                for tree in grid[i][j]:
                    if tree % 5 == 0:
                        for k in range(8):
                            nr = i + row[k]
                            nc = j + col[k]
                            if not (0 <= nr < n and 0 <= nc < n):
                                continue
                            grid[nr][nc].append(1)

    # 4. 겨울엔 양분 추가.
    for i in range(n):
        for j in range(n):
            nutrition[i][j] += fill[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            ans += len(grid[i][j])
print(ans)
