'''
[문제 설명]
    명예의 전당에 학생들 사진이 올라간다.
    1. 학생이 추천 받으면 추천 받은 학생은 게시된다.
    2. 비어있는 사진틀이 없으면 추천횟수가 적은 학생 사진이 out, 그리고 추천받은 새로운 학생이 올라간다.
        2-2. 동점자가 있으면 오래된 사진을 삭제
    3. 이미 걸려있는데 또 추천을 받으면 누적해서 점수가 증가한다.
    4. 사진이 삭제될 경우 추천횟수는 0으로
[입력]
    1. 사진틀의 갯수 N = 배열의 크기
    2. 총 추천횟수
    3. 추천하는 학생 번호
[출력]
    액자에 걸려있는 학생

[구상]
    class와 pq를 사용한다.
    student class엔  num, day, love을 변수로 가진다(학생번호, 등록날짜, 추천수)
    우선순위는 1. love가 낮고 2. day가 낮은 순이다(day가 낮을 수록 오래됐음)

'''
import heapq


class Student:
    def __init__(self,num, day,love):
        self.num = num
        self.day = day
        self.love = love

    def __lt__(self, other):
        if self.love == other.love:
            return self.day < other.day
        else:
            return self.love < other.love


n = int(input())
people_num = int(input())
people_list = list(map(int, input().split()))
q = []
for i in range(people_num):
    # i가 day가 될거임.

    people = people_list[i]
    # 1. 학생이 추천 받으면 추천 받은 학생은 게시된다.
    if(not q): # 비어있으면 바로 넣어도됨
        heapq.heappush(q, Student(people, i, 1)) # 학생 번호, 날짜, 좋아요 수
    else:
        # 이미 투표받았는지 확인
        isDuple = False
        for student in q:
            if(student.num==people):
                student.love +=1
                isDuple = True
                break
        if(not isDuple): # 들어갈 수 있으면 들어가고 못들어가면 뺀 다음에 넣어줌
            if(len(q)<n):
                heapq.heappush(q, Student(people,i,1))
            else:
                heapq.heappop(q)
                heapq.heappush(q, Student(people, i, 1))
    for student in q:
        print("학생번호:",student.num,"등록일:",student.day, "추천수:", student.love)
    print("========================")

ans = []
while q:
    ans.append(heapq.heappop(q).num)
ans.sort()

for x in ans:
    print(x,end = " ")