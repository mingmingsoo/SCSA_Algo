'''
[문제설명]
    1에 위치한 하노이탑을 3으로 모두 이동시키는 데
    최소 이동 횟수는?
'''

n = int(input()) # 탑의 높이

print(2**(n)-1)
def hanoi(depth, f,m,t):
    if(depth ==1):
        print(f,t)
        return
    hanoi(depth-1,f,t,m)
    print(f, t)
    hanoi(depth-1,m,f,t)
hanoi(n,1,2,3) # n, from, middle, to



