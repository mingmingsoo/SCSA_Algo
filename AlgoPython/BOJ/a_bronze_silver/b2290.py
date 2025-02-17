'''
예상시간 30

[문제설명]
    정수 s, n 이 들어왔을 때 출력해라..?ㅋㅋㅋ
[구상]
    길이가 s인 -와 |를 사용하고
    각 숫자는 모두 s+2 가로, 2s+3 세로로 이루어짐
'''

s, num = input().split()
s = int(s)
num = list(map(int,num))
print(s, num)
arr = [[] for i in range(2*s+3)]
for i in range(2*s+3):
    for ele in num:
        if(ele==1):
            arr.append(" ")
