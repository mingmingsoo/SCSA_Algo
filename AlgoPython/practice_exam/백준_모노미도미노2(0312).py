'''
# 코드트리 2차원 테트리스
2025.03.31.월
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 2회
    문제 시작 16:50
    1차 제출  17:16
    문제 종료 17:19

    총 풀이시간 29분
        50~53   : 문제 이해, 손코딩(3)
        53~56   : 탑다운 설계(3)
        56~08   : location 설계(12)
        08~09   : delete 설계(1)
        09~10   : special 설계(1)
        10~16   : 문제 예시 검증(6)
        16      : 틀렸습니다!
        16~19   : 틀린 테케 검증(3)
                    어.. 두줄이 한번에 안지워짐 ㅠㅠ 디버깅 시작
                    delete 함수에서 pop 할 때 앞에서부터 봐줘야하는데
                    뒤에서부터 봐줘서 검사를 못했음!! 앞에서부터 보는 걸로 수정


  메모리 23 MB
  시간 226 ms

  회고
    1. 너 왜 검증안해 죽을래???????????????????????????????????????????????..............
        N회차도 긴장해라.................

'''


block_num = int(input())
m, n = 4, 6
yel = [[0] * m for i in range(n)]
red = [[0] * m for i in range(n)]
sc = 0


def location():
    if shape == 1:
        # 그냥 네모
        nr = n - 1
        for i in range(n):
            if yel[i][c]:
                nr = i - 1
                break
        yel[nr][c] = 1

        nr = n - 1
        for i in range(n):
            if red[i][3 - r]:
                nr = i - 1
                break
        red[nr][3 - r] = 1

    elif shape == 2:
        # 가로
        nr = n - 1
        for i in range(n):
            if yel[i][c] or yel[i][c + 1]:
                nr = i - 1
                break
        yel[nr][c] = yel[nr][c + 1] = 1

        nr = n - 1
        for i in range(n):
            if red[i][3 - r]:
                nr = i - 1
                break
        red[nr][3 - r] = red[nr - 1][3 - r] = 1

    elif shape == 3:
        # 세로
        nr = n - 1
        for i in range(n):
            if yel[i][c]:
                nr = i - 1
                break
        yel[nr][c] = yel[nr - 1][c] = 1

        nr = n - 1
        for i in range(n):
            if red[i][3 - r] or red[i][3 - r - 1]:
                nr = i - 1
                break
        red[nr][3 - r] = red[nr][3 - r - 1] = 1


def delete(grid):
    global sc
    for i in range(n):
        if grid[i].count(1) == 4:
            sc += 1
            grid.pop(i)
            grid.insert(0, [0] * 4)


def special(grid):
    cnt = 0
    for i in range(2):
        if 1 in grid[i]:
            cnt += 1
    for _ in range(cnt):
        grid.pop()
        grid.insert(0, [0] * 4)


for b in range(block_num):
    shape, r, c = map(int, input().split())
    location()  # 위치시키기
    delete(yel)  # 한 줄 채워진 애들 지우기 + 점수
    delete(red)
    special(yel)
    special(red)


print(sc)
print(sum(map(sum, red)) + sum(map(sum, yel)))



'''
# 20061 백준 새로운 게임2
# 체감난이도 골2

# 문제 풀고 나서 기록

    문제 시작 14:00
    문제 종료 16:08
    총 풀이시간 128분(5차제출)
        00~10   : 문제 이해(10)
        10~14   : 문제 구상 및 초기 주석(4)
        14~18   : 탑다운 설계(4)
        18~30   : location 설계(12)
        30~51   : delete 설계(28)
        51~03   : special 설계
        03      : 1차 제출 -> 틀
                    디버깅 -> 스페셜 로직 오류 확인
        03~22   : 2차 제출 -> 틀
                    모든게 의심스러워져서
                    점수얻고 지운다음에 스페셜 지운다음에 떨어뜨리는건가??
                    해서 메서드 순서 수정
                    delete -> special -> fall 로 수정
        22~44   : 3차 제출 -> 틀
                for j in range(n - 1, -1, -1):를 혹시몰라서
                for j in range(n - 1, 5, -1): 로 바꿈
                이거 때문에 틀린게 아니라 delete fall 순서 차이임
        44~53   : 4차 제출 -> 틀
                진짜 내 눈에 틀린게 없어보임
                delete -> fall -> special 로 수정
        53~ 08  : 5차 제출, 성공

    회고
    1. 처음부터 꼼꼼히짜서 틀리는 일이 없게하자.
    2. 탑다운 설계는 잘 했지만..... 세부 로직을 꼼꼼히 못짠게 아쉽네
    3. 문제 설계 전에 어떻게 해야 편하게, 효율적으로 짤 수 있는지 고민좀 해보자
    4. 10*10 말고 블루, 그린 배열 만들어서 다시 풀어보기

    메모리 114056 KB
    시간 316 ms

    회고


# 문제 풀고나서 기록
문제설명
    블록의 정보를 줄 때 구현해라.
입력
    블록갯수
    블록정보, 어디에 놓을지
출력
    블록을 모두 놓았을 때 얻은 점수
    파/초에 들어있는 타일의 갯수
구상
    시뮬레이션..
주의할점
    밑에가 없을 떄까지 떨어지는게 아님(맨 밑 그림)
    점수는 한 줄이 모두 없어질때
필요한 변수
    location() 해당하는 위치로 옮겨줌
    delete() 한 줄이 없어질 수 잇는지 -> 갯수세서 그만큼만 땡겨주기
    fall()
    special() 스페셜 공간에 놓아졌는지
    special_fall()

디버깅용 테케
5
3 2 0
3 1 0
3 2 0
3 1 0
2 2 0

5
2 0 0
2 0 1
2 0 0
2 0 1
3 0 1

5
3 0 0
3 0 1
3 0 2
3 0 0
3 0 3

5
2 0 0
2 1 0
2 2 0
2 0 0
2 3 0
'''
n = 10
grid = [[0] * n for i in range(n)]
block_num = int(input())
score = 0

def location(r, c, shape):
    if shape == 1:  # 하나짜리
        # 초록
        nr = n - 1  # 아무것도 없었으면 바닥에!
        for i in range(r, n):
            if grid[i][c] == 1:  # 있었으면 그 전에!
                nr = i - 1
                break
        grid[nr][c] = 1
        # 파랑
        nc = n - 1
        for j in range(c, n):
            if grid[r][j] == 1:
                nc = j - 1
                break
        grid[r][nc] = 1
    elif shape == 2:  # 가로 두개
        # 초록
        nr = n - 1
        for i in range(r, n):
            if grid[i][c] == 1 or grid[i][c + 1] == 1:
                nr = i - 1
                break
        grid[nr][c], grid[nr][c + 1] = 1, 1
        # 파랑
        nc = n - 1
        for j in range(c, n):
            if grid[r][j] == 1:
                nc = j - 1
                break
        grid[r][nc], grid[r][nc - 1] = 1, 1

    elif shape == 3:  # 세로 두개
        # 초록
        nr = n - 1
        for i in range(r, n):
            if grid[i][c] == 1:
                nr = i - 1
                break
        grid[nr][c], grid[nr - 1][c] = 1, 1
        # 파랑
        nc = n - 1
        for j in range(c, n):
            if grid[r][j] == 1 or grid[r + 1][j] == 1:
                nc = j - 1
                break
        grid[r][nc], grid[r + 1][nc] = 1, 1


def delete():
    global score, green_line, blue_line
    for i in range(n - 1, 5, -1):
        if grid[i][:4].count(1) == 4:
            green_line += 1
            grid[i][:4] = [0, 0, 0, 0]

    for j in range(n - 1, 5, -1):
        cnt = 0
        for i in range(4):
            if grid[i][j] == 1:
                cnt += 1
        if cnt == 4:
            blue_line += 1
            for i in range(4):
                grid[i][j] = 0

    score += green_line
    score += blue_line

def special():
    green_special = 0
    for i in (4, 5):
        if grid[i][:4].count(1) > 0:
            green_special += 1

    for i in range(n - 1, n - 1 - green_special, -1):
        for j in range(4):
            grid[i][j] = 0

    # 땡겨줌
    for w in range(green_special):
        for i in range(n - 1, 0, -1):
            for j in range(4):
                grid[i][j], grid[i - 1][j] = grid[i - 1][j], grid[i][j]  # 땡겨준다.

    blue_special = 0
    for j in (4, 5):
        for i in range(4):
            if grid[i][j] == 1:
                blue_special += 1
                break

    for j in range(n - 1, n - 1 - blue_special, -1):
        for i in range(4):
            grid[i][j] = 0

    for w in range(blue_special):
        for j in range(n - 1, 0, -1):
            for i in range(4):
                grid[i][j], grid[i][j - 1] = grid[i][j - 1], grid[i][j]  # 땡겨준다.


def fall():
    for w in range(green_line):
        for i in range(n - 1, 0, -1):
            if grid[i][:4] == [0, 0, 0, 0]:
                for j in range(4):
                    grid[i][j], grid[i - 1][j] = grid[i - 1][j], grid[i][j]
    for w in range(blue_line):
        for j in range(n - 1, 0, -1):
            cnt = 0
            for i in range(4):
                if grid[i][j] == 0:
                    cnt += 1
            if cnt == 4:
                for i in range(4):
                    grid[i][j], grid[i][j - 1] =  grid[i][j - 1], grid[i][j]


for block in range(block_num):
    green_line=0
    blue_line = 0
    shape, r, c = map(int, input().split())
    location(r, c, shape)
    delete()
    fall()
    special()

print(score)
total = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            total += 1
print(total)
