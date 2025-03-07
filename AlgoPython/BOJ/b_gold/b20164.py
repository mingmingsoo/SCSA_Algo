'''
홀수 갯수 적는다
한자리수면 return
두 자리이면 두개 더한다
세개 이상이면 3개로 분할.

분할을 어케 할 것이냐......

세개를 더한 값임
세개를 더한 값임
세개를 더한 값임
세개를 더한 값임
세개를 더한 값임
세개를 더한 값임세개를 더한 값임세개를 더한 값임
세개를 더한 값임세개를 더한 값임세개를 더한 값임
세개를 더한 값임세개를 더한 값임세개를 더한 값임세개를 더한 값임세개를 더한 값임세개를 더한 값임
세개를 더한 값임세개를 더한 값임세개를 더한 값임

'''

n = input()

maxi = 0
mini = int(1e9)


def dfs(n, score):
    global maxi, mini

    if len(n) == 1:
        if int(n) % 2 == 1:
            mini = min(mini, score + 1)
            maxi = max(maxi, score + 1)
        else:
            mini = min(mini, score)
            maxi = max(maxi, score)

    ele_score = 0
    for num in n:
        if int(num) % 2 == 1:
            ele_score += 1

    if len(n) == 2:
        new_num = int(n[0]) + int(n[1])
        dfs(str(new_num), score+ele_score)
        return

    if len(n) > 2:
        for i in range(1, len(n)):
            for j in range(i + 1, len(n)):
                num1 = n[0:i]
                num2 = n[i:j]
                num3 = n[j:]
                new_num = int(num1) + int(num2) + int(num3)
                dfs(str(new_num), score+ele_score)


dfs(n, 0)
print(mini, maxi)
