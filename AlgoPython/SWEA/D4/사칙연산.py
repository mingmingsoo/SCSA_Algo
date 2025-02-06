def ord(n):
    global ans
    if (lefts[n]==0 or rights[n]==0):  # 말단노드면 값내놔
        return arr[n]
    left_num = ord(lefts[n])
    right_num = ord(rights[n])
    if (arr[n] == "+"):
        ans = (left_num + right_num)
    elif (arr[n] == "-"):
        ans = (left_num - right_num)
    elif (arr[n] == "/"):
        ans = (left_num / right_num)
    elif (arr[n] == "*"):
        ans = (left_num * right_num)
    return ans
T = 10
for tc in range(T):
    '''
    중위순회
    '''

    N = int(input())

    lefts = [0] * (N + 1)
    rights = [0] * (N + 1)
    arr = [0] * (N + 1)

    for i in range(N):
        tmp = list(input().split())
        if (len(tmp) == 4):
            num, cal, left, right = int(tmp[0]), tmp[1], int(tmp[2]), int(tmp[3])
            arr[num] = cal
            lefts[num] = left
            rights[num] = right
        else:
            num, number = int(tmp[0]), int(tmp[1])
            arr[num] = number
    ans = 0
    ord(1)
    print(f"#{tc+1} {int(ans)}")
