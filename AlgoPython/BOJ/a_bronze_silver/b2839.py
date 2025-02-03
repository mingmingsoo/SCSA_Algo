'''
3x+5y = 18 이 되는 x,y 찾기
단 x+y가 작아야함.
'''
num = int(input())
ans = 1001
for i in range(num):
    for j in range(num):
        if(3*i+5*j == num):
            ans = min(ans, i+j)
if(ans == 1001):
    ans = -1
print(ans)