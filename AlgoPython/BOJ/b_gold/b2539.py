n, m = map(int, input().split())
limit = int(input())
wrong_num = int(input())
wrong_lst = []
start = 1
for w in range(wrong_num):
    r, c = map(int, input().split())
    start = max(start, r)
    wrong_lst.append((r, c))

wrong_lst.sort(key=lambda x: (x[1], x[0]))

end = min(n, m)
ans = 0


def mozic(size):
    cnt = 0
    j = 0
    for r, c in wrong_lst:
        if c > j:
            cnt += 1
            j = c + size - 1
    if cnt > limit:
        return False
    return True


while start <= end:
    middle = (start + end) // 2

    if mozic(middle):  # 가려지냐?
        ans = middle
        end = middle - 1
    else:
        start = middle + 1
print(ans)