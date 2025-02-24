'''
제출횟수 4회
1. 메모리초과
2. 시간초과
3. 시간초과

위 3번은 모든 점을 탐색했는데 범위에 맞춰서 가려고 하는데만 가면 된다.

문제 설명
    분할...정복...
    size가 2가 될때까지 계속 분할한다. -> 아니 1이될때까지
    r행 c열을 몇번째로 방문하는지 출력-> 넘버링을 하면 됨 -> 이러면 시간초과남
    범위에 맞춰 가고 ans를 더해주는 식으로.
입력
    n,r,c
'''

N, er, ec = map(int, input().split())

size = 2 ** N

num = 0
ans = 0
find = False


def z(r, c, size):
    global num, ans, find
    if find:
        return
    if (size == 1):
        return
    # 필요한데만 간다.
    if (er < r + size // 2 and ec < c + size // 2):
        z(r, c, size // 2)
    elif er < r + size // 2 and ec >= c + size // 2:
        z(r, c + size // 2, size // 2)
        ans += (size * size) // 4 * 1 # 위치에 따라 값을 더해줬음
    elif er >= r + size // 2 and ec < c + size // 2:
        z(r + size // 2, c, size // 2)
        ans += (size * size) // 4 * 2
    else:
        z(r + size // 2, c + size // 2, size // 2)
        ans += (size * size) // 4 * 3


z(0, 0, size)

print(ans)
