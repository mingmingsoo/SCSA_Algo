T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input()))

    dict = {}

    for i in arr:
        dict[i] = 0
    for i in arr:
        dict[i] = dict[i]+1
    # print(dict)
    max = 0
    ans = 0
    for key, value in dict.items():
        # print(k, value)
        if(value >=max):
            max = value
            ans = max(ans, key)
            # if(ans < key): # 왜 ans = max(ans, key)가 안되지?
            #     ans = key
    print(f'#{t+1} {ans} {max}')
