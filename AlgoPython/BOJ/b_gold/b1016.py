'''
에라 어쩌구체

sqrt 해서 시간복잡도 낮추는 방법이 아닌
배수판정으로 시간복잡도 낮추는 방법.

# 1000000000000 1000001000000
'''
import sys
input = sys.stdin.readline

min, max = map(int, input().split())
total = max-min+1

prime = [i for i in range(min, max+1)] # min~ max의 배열을 생성

end = int(max**(1/2))+1 # 소수 수열을 탐색할 끝 점 지정
# max의 루트값까지만 가도 배수 판정 가능함.

isPrime = [True] * (end+1)
for i in range(2, end):
    if isPrime[i]:
        for j in range(i*i, end+1,i):
            isPrime[j] = False


for i in range(2,end):
    if(isPrime[i]):
        square = i*i # 제곱수
        start = ((min + square - 1) // square) * square
        for j in range(start, max+1, square): # 제곱수에 0 처리 하기.
            if(j-min>=0): # 이거 조건 없어서 배열의 -1 로 뒤로가서 안됐었음
                prime[j-min]= 0


square = 0
for ele in prime:
    if(ele==0):
        square+=1
print(total - square)
