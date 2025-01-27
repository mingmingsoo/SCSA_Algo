fibo = [0] * 41
fibo[0] = 0
fibo[1] = 1

for i in range(2, 41):
    fibo[i] = fibo[i-1]+fibo[i-2]

T = int(input())
for t in range(T):
    n = int(input())
    if(n==0):
        print(1, 0)
    elif (n==1):
        print(0, 1)
    else:
        print(fibo[n - 1], fibo[n])



