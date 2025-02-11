'''
입력
    왼-점수 우-칼로리

출력
    칼로리가 limit "이하"인 애들 중에 점수가 높은 애들

고려조건
    부분집합처럼 생각해서 모든 경우의 수를 따져야한다.

백트래킹
    칼로리가 limit 이상이면 return

'''
T = int(input())
for tc in range(T):
    n, limit = map(int, input().split())
    score_list = []
    cal_list = []
    for i in range(n):
        s, c = map(int, input().split())
        score_list.append(s)
        cal_list.append(c)

    max_score = 0


    def btk(idx, score, cal):
        global max_score

        if (cal <= limit):
            max_score = max(score, max_score)  # return 하면 안됨.
        if (cal > limit):
            return  # 이건 해야됨
        if (idx == n):
            return

        btk(idx + 1, score + score_list[idx], cal + cal_list[idx])
        btk(idx + 1, score, cal)


    btk(0, 0, 0)  # idx, 점수, 칼로리
    print(f"#{tc+1} {max_score}")