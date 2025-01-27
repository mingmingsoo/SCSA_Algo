T = int(input())

for tc in range(T):
    long, short = input().split()

    idx = 0
    cnt = 0
    while (idx < len(long)):
        # print(idx, cnt)
        if (long[idx:idx + len(short)] == short):
            cnt += 1
            idx += len(short)
        else:
            idx += 1
            cnt += 1
    print(f"#{tc+1} {cnt}")



