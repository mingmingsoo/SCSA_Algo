'''
[문제설명]
    n보다 크고! 2n보다 작거나 같은! 소수의 갯수를 구해라
[구상]
    테케 밖에서 먼저 프라임 여부를 확인하고
    범위에 해당하는 소수만 확인해주면 된다.

    배수판정법으로 풀어보기
'''
import math
size= 123_456*2+1
# size= 15
prime = [True]*size # 일단 다 소수야


for i in range(2, int(math.sqrt(size))+1): # 구하려는 값의 루트까지만 가도 배수를 판정할 수 있어
    if(not prime[i]): # 이미 배수면 넘어가!
        continue
    for j in range(i*i, size, i): # 나 제외하고 곱해지는 애들은 배수야
        prime[j] = False # 나는 배수야

while True:
    num = int(input())
    if(num==0):
        break
    ans = 0
    for i in range(num+1,2*num+1):
        if(prime[i]):
            ans+=1
    print(ans)