T = int(input())
for tc in range(T):
    '''
    모든 경우의 수 찾기인데...
    숫자가 작아서 완탐하겠습니다
    '''
    n, num = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k] == num):
                    ans += 1
    print(f"#{tc+1} {ans}")