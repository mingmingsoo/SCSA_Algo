'''
[문제설명]
    n보다 크고! 2n보다 작거나 같은! 소수의 갯수를 구해라
[구상]
    테케 밖에서 먼저 프라임 여부를 확인하고
    범위에 해당하는 소수만 확인해주면 된다.
'''
import math
size= 123_456*2+1
# size= 15
prime = [True]*size
for i in range(2, size):
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j ==0):
            prime[i] = False
            break



while True:
    num = int(input())
    if(num==0):
        break
    ans = 0
    for i in range(num+1,2*num+1):
        if(prime[i]):
            ans+=1
    print(ans)