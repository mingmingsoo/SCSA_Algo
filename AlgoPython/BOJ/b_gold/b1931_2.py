'''
[문제 설명]
    컨테이너 운반과 동일 문제
    회의실을  최대한 비지 않게 채워라.

[구상]
    종료시간으로 오름차순, 시작시간으로 오름차순해서 가능한 갯수를 샌다.
    종료가 빠른게 장땡이다.
'''

n = int(input())
meeting = []
for i in range(n):
    s , e = map(int, input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x:(x[1],x[0]))
# print(meeting)
end = 0
cnt = 0
for s, e in meeting:
    # print(end)
    if(s>=end):
        cnt+= 1
        end = e
print(cnt)


