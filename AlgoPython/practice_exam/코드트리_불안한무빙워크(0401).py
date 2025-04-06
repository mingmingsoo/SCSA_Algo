'''
# 코드트리 불안한 무빙워크
2025.04.01.월
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 3회.............................................
    문제 시작 21:23
    1차 제출  21:45 [틀린이유: 올릴 때 q검사 양수인지 검사 해야하는데 안했음 미친거지 테케는 어케 나왔냐]
    문제 종료 21:49

    총 풀이시간 26분
        23~30 : 문제 이해
        30~45 : 1차 제출
                -> 시간초과
        45~49 : 3번테케 디버깅
                 무한루프 도는 거 확인
                 q 찍어보니까 q가 엄청난 음수값임
                 아.. 올릴 때 q 부호 검사를 안했네 - > 수정!

  메모리 18 MB
  시간 88 ms

    회고
        0. 백준보다 문제가 친절한듯 ?? 이해가 잘 됐음.
        1. 검증을 안하시니까 틀리시죠 이 자식아...............

'''

from collections import deque

n, limit = map(int, input().split())
q = deque(map(int, input().split()))

time = 0
ans = 0


def end():
    cnt = q.count(0)
    if cnt >= limit:
        return True
    return False


people = [0] * n
while True:
    time += 1
    # 1. 무빙워크 한 칸 회전
    q.rotate(1)
    people.insert(0, people.pop())
    if people[n - 1]:
        people[n - 1] = 0

    # 2. 쩜푸
    for i in range(n - 2, -1, -1):
        if people[i] and not people[i + 1] and q[i + 1] > 0:
            people[i], people[i + 1] = people[i + 1], people[i]
            q[i + 1] -= 1
    if people[n - 1]:
        people[n - 1] = 0
    # 3. 올려!
    if not people[0] and q[0] > 0:
        people[0] = 1
        q[0] -= 1
    if people[n - 1]:
        people[n - 1] = 0
    # 4. 검증
    if end():
        ans = time
        break

print(time)
