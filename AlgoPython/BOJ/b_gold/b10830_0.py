# 분할정복 연습

c = 2 # 2의
n = 10 # 10승

def mypow(c,n):
    if(n ==1):
        return c

    if(n%2 ==0):
        tmp = mypow(c,n/2) * mypow(c,n/2)
        print(tmp)
        return tmp
    else:
        tmp = mypow(c,((n-1)/2)) * mypow(c,((n-1)/2)) * c
        print(tmp)
        return tmp


print(mypow(c,n))
