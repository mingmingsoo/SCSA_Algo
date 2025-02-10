
'''
별의 별 큰 숫자를 넣어도 바로 출력되는데 시간초과 나는중 ㅠㅠ
1021321314 24913213 134342313
맞췄는데 왜 되는지 모르겠음
tmp = my_pow(a, (b - 1) // 2) %c 이게 하면 왜빨라지지??
-> 파이썬은 숫자를 만들 때 큰 숫자도 메모리를 붙혀서 시간과 메모리를 많이 잡아먹는다고함.
그래서  my_pow(a, (b - 1) // 2) %c  를 하면서 숫자를 줄여줘서 시간이 빨라진 것
'''
import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
cnt = 0

def my_pow(a, b):
    global cnt
    cnt+=1
    if (b <= 1):  # == 1이 아니라 1보다 작아야함! 0승이 들어갈 수도 있음
        return a
    if (b % 2 == 0):  # 짝수면
        tmp = my_pow(a, b // 2) %c
        return tmp * tmp
    else:
        tmp = my_pow(a, (b - 1) // 2)%c
        return tmp * tmp * a


ans = my_pow(a, b)
print(ans % c)
print(cnt)