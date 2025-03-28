'''
내 코드 시간복잡도가 큰 이유:
    이차원배열로 관리하면 n*n(50*50)
    근데 나는 M*M(50*50*50*50)
    운이 좋아서 첫번째 코드는 통과한거임.

     4 ≤ N ≤ 50
     0 ≤ M ≤ N^2

    귀찮아도 2차원 배열로 관리했었어야함.
'''


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
