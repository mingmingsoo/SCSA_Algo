

n = int(input())
arr = list(int(input()) for i in range(n))
arr.append(1000000001)
'''
우큰수랑 비슷하네
뒤에서부터 나보다 가장 가까이 큰애의 인덱스를 찾아서
stk에 넣어줌..

그 대신 마지막에 엄청 큰 빌딩이 있다고 생각해야
뒤에서 두번째 애의 처리를 해줄 수 있음..

틀렸던 이유: 숫자 잘못봐서 80,001 을 추가했음

6
10
3
7
4
90000
2

이면 답은 5인데 80001을 넣으면 4가 나옴

6
10
3
7
4
900000
2
80001
[4, 2, 4, 4, 0, 6, 0] <- 80001 일때, 5번째 애가 아무것도 못본다고 뜸
[4, 2, 4, 4, 6, 6, 0] <- 정답일 때

'''

n+=1
stk = [n-1]
ans = [0]*(n)

for i in range(n-2,-1,-1):
    while stk and arr[i]> arr[stk[-1]]:
        stk.pop()
    if(stk):
        ans[i] = stk[-1]
    stk.append(i)
total = 0
for i in range(n-1):
    if(ans[i]>0):
        total +=(ans[i]-i-1)
print(total)


