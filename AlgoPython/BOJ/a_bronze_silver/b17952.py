'''
1. 과제는 최신순, 과제 받으면 바로
2. 과제 도중 새로운 과제 오면 하던 과제 중단하고 새로운 과제 (으휴)
3. 새로운 과제 끝나면 이전 과제 마저함
    과제 점수를 구해라

입력
    이번 학기 몇 분?
    n 분째에 과제 주어짐
    1 A T : 과제 만점 A 점이고 해결하는데 T 분
    0 : 과제 안줌
'''
time = int(input())

homework = []
ans = 0
for t in range(time):
    tmp = list(map(int, input().split()))
    if len(tmp) > 1:
        score, long = tmp[1], tmp[2]
        if long - 1 == 0:
            ans += score
        else:
            homework.append((score, long - 1))
    else:
        if homework:
            score, long = homework.pop()
            if long - 1 == 0:
                ans += score
            else:
                homework.append((score, long - 1))

print(ans)
