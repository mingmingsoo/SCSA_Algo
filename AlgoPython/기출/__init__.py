'''
열을 몇개 갈 수 있냐를 파악해야함.
'''

n, m = map(int, input().split())
L, R = map(int, input().split())
grid = [list(map(int, input())) for i in range(n)]


def find():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                grid[i][j] = 0
                return i, j


r, c = find()
