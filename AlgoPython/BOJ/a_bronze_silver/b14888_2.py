'''
굳이 순열로 생각하지말고
백트래킹으로 해결하기.
'''
n = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))
mini = 1000000000+1 # 헤헤 십억이구나
maxi = -mini


def oper(before, idx, i):
    if(i==0):
        return before + arr[idx+1]
    elif(i==1):
        return before - arr[idx+1]
    elif(i==2):
        return before * arr[idx+1]
    elif(i==3):
        if(before<0 and arr[idx+1]>0):
            before *= -1
            mok = before//arr[idx+1]
            return -mok
        return before // arr[idx+1]

def btk(idx, rlt):
    global mini, maxi
    if(idx == n-1):
        mini = min(mini, rlt)
        maxi = max(maxi, rlt)
        return
    for i in range(len(cal)):
        if(cal[i]<=0):
            continue
        cal[i] -=1
        btk(idx+1, oper(rlt,idx,i))
        cal[i]+=1

btk(0,arr[0])
print(maxi)
print(mini)
