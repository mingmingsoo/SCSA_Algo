'''
16진수가 뭔데
서현이 천재세요
'''

T = int(input())
for tc in range(T):

    n, num = map(int, input().split())
    arr = list(input())

    ro = n // 4
    l = n // 4
    password = set()
    # 일단 0회전
    for i in range(0, n, l):
        tmp = arr[i:i + l]
        password.add(tuple(tmp))

    # 그리고 나머지 회전
    for _ in range(ro - 1):
        arr.insert(0, arr.pop())
        for i in range(0, n, l):
            tmp = arr[i:i + l]
            password.add(tuple(tmp))

    password = sorted(list(password), reverse=True)
    string = password[num - 1]

    ans = 0
    for i in range(l - 1, -1, -1):
        num = int("0123456789ABCDEF".index(string[i]))
        ans += num * 16 ** (l - i - 1)
    print(f"#{tc + 1} {ans}")
