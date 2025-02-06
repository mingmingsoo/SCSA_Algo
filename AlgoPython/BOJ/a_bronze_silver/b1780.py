'''
종이가 모두 같으면 그대로 사용
아니면 종이를 9개로 자름 -> 위 반복
-1,0,1 종의 갯수를 구하라
'''

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

# n -> sqrt(n) -> 사이즈를 줄여나감.

ans = [0] * 3  # -1,0,1


def valid(size, start_r, start_c):
    first = grid[start_r][start_c]
    for i in range(start_r, start_r + size):
        for j in range(start_c, start_c + size):
            if (grid[i][j] != first):
                return -2
    return first


def recur(size, start_r, start_c):
    if (size == 1):
        ans[grid[start_r][start_c]+1] += 1
        return

    # 검사하고 아니면 재귀탐.
    # print(size, start_r, start_c)
    num = valid(size, start_r, start_c)
    if (num == -2):
        next_size = int(size / 3 ) # 이거때문에 2번 틀렸음 sizze**(1/2)로 해서 틀림! 나누기 3임
        for i in range(0, size, next_size):
            recur(next_size, start_r, start_c + i)
        for i in range(0, size, next_size):
            recur(next_size, start_r + next_size, start_c + i)
        for i in range(0, size, next_size):
            recur(next_size, start_r + next_size * 2, start_c + i)
    else:
        ans[num + 1] += 1


recur(n, 0, 0)  # size, start_r, start_c
for x in ans:
    print(x)
