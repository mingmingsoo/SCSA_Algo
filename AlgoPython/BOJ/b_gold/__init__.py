
from itertools import combinations


def match(order, ans):
    if order == 15:
        possible_set.add(ans)
        print(ans)
        return

    x, y = game_order[order]

    # x가 이기는 경우
    match(order+1, ans + 10**(17-3*x) + 10**(17-3*y-2))

    # y가 이기는 경우
    match(order + 1, ans + 10**(17-3*x-1) + 10**(17-3*y-1))

    # 비기는 경우
    match(order + 1, ans + 10**(17-3*x-2) + 10**(17-3*y))


arr = [list(map(int, input().split())) for _ in range(4)]
result_board = [[0]*3 for _ in range(6)] # A~F Win, 무승부, Lose
game_order = list(combinations(range(6), 2))
print(game_order)
possible_set = set()
match(0, 0)
print(possible_set)

for lst in arr: # 총 4개의 결과
    print(lst)
    val = lst[0]
    for i in range(1, 18):
        val = val * 10 + lst[i]
    print(1 if val in possible_set else 0, end = ' ')