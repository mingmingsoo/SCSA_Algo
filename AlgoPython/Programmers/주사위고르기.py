'''
문제설명
    완탐인데..
    1. 주사위를 뽑는 것은 조합임
    2. 주사위를 뽑고나서 주사위를 선택하는 것은 순열임
'''

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
n = len(dice)
m = n // 2
# 주사위 조합
A = [0] * (m)
ans = []
awin = 0
sel = [0] * n


def subset(A, B, idx):
    global sel, awin, dice, n

    if idx == n:
        ascore = 0
        bscore = 0
        for i in range(n//2):
            ascore += dice[A[i]][sel[i]]
        for i in range(n//2,n):
            bscore += dice[B[i - n // 2]][sel[i]]
        if ascore > bscore:
            awin += 1
        return

    for i in range(6):
        sel[idx] = i
        subset(A, B, idx + 1)

def combi(sidx, idx):
    global sel, arr, awin
    if sidx == m:
        # 이제 여기서 또한 승패를 봐줘야함..ㅋ...ㅇ.ㅇ.ㅇ. 진짜 봐야하나?ㅠㅠ
        B = []
        for i in range(n):
            if i not in A:
                B.append(i)

        sel = [0] * n
        awin = 0
        subset(A, B, 0)  # A, B, aidx, bidx, asum, bsum

        ans.append((A[:], awin))

        return

    if idx == n:
        return

    A[sidx] = idx
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)

real_ans = []
combi(0, 0)
ans.sort(key=lambda x:x[1], reverse=True)
if n == 2:
    real_ans.append(ans[0][0][0] + 1)
else:
    for i in range(n // 2):
        real_ans.append(ans[0][0][i] + 1)

print(real_ans)
