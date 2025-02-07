'''
((()))
((( 까지는 곱해주다가
) 만났을 때 ) 전이 ( 면은 ans에 tmp 더해주고 tmp// num 해주면서 원상복구 시킴



'''


arr = list(input())
stk = []

ans = 0
tmp = 1

for i in range(len(arr)):
    s = arr[i]
    print(ans)
    if(s=="("):
        stk.append("(")
        tmp *= 2
    elif(s == "["):
        stk.append("[")
        tmp *= 3

    ## 닫히는 애들 검사
    elif(s == ")"):
        if(i>0 and arr[i-1]=="("):
            ans += tmp
        stk.pop()
        tmp = tmp // 2
    elif(s == "]"):
        if(i>0 and arr[i-1]=="["):
            ans += tmp
        stk.pop()
        tmp = tmp // 3
if(stk):
    ans = 0
print(ans)