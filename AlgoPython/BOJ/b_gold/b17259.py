'''
선물이 넘쳐흘러 다시 풀기

5 1 2
1 0 1

정답2
'''


class Person:
    def __init__(self, r, c, time):
        self.r = r
        self.c = c
        self.time = time
        self.ing = 0


n, people_num, present_num = map(int, input().split())
people_list = []
for i in range(people_num):
    r, c, t = map(int, input().split())
    people_list.append(Person(r, c + 1, t))
row = [1, 0, -1]
col = [0, 1, 0]
grid = [[0] * (n + 1) for i in range(n)]
grid[0][0] = present_num  # 선물 놓는다.
out = 0
for p in range(n * 2 + (n - 2) + present_num):
    # 1. 선물이 있으면 올리기
    if grid[0][0] > 0:
        grid[0][1] = 1
        grid[0][0] -= 1

    # 3. 근방에 직원 있으면 포장
    for people in people_list:
        # 포장중이 아닌 애들은 포장!
        if people.ing == 0:
            for k in range(3):
                nr = people.r + row[k]
                nc = people.c + col[k]
                if not (0 <= nr < n and 0 <= nc < n + 1):
                    continue
                if grid[nr][nc] > 0:
                    grid[nr][nc] = 0
                    people.ing += 1
                    break
        # 나머지들은 마저 포장!
        else:
            people.ing += 1

    for people in people_list:
        if people.ing >= people.time:
            people.ing = 0

    # 2. 이동
    # 뒤에서 부터 당기기
    for j in range(n):
        grid[n - 1][j] = grid[n - 1][j + 1]
    for i in range(n - 1, 0, -1):
        grid[i][n] = grid[i - 1][n]
    for j in range(n, 1, -1):
        grid[0][j] = grid[0][j - 1]
    grid[0][1] = 0

    # 4. 떨어지는 갯수 세기
    if grid[n - 1][0] > 0:
        out += 1
        grid[n - 1][0] = 0
print(present_num - out)
