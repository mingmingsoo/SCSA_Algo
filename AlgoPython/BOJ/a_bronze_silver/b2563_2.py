'''
메모리 109544KB
시간 96ms
저번 풀이와 다른점
: 이중 포문으로 배열을 채운뒤 또 이중포문으로 개수를 카운팅 하지 않고,
1을 채우면서 1로 채울수 있으면 카운트 +1 을 했습니다!
-> 속도 차이는 그닥.. 없습니다
'''
n = int(input())
grid = [[0] * 101 for i in range(101)]

ans = 0
for _ in range(n):
    r, c = map(int, input().split())

    for i in range(r, r + 10):
        for j in range(c, c + 10):
            if (grid[i][j] == 0):
                ans += 1
                grid[i][j] = 1
print(ans)
