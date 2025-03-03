'''
b1065
숫자가 등차수열을 이루면 갯수를 출력
'''

n = int(input())
ans = 0
for i in range(1,n+1):
    string = str(i)
    if len(string) == 1:
        ans+=1
        continue
    else:
        diff = int(string[0])-int(string[1])

        for j in range(1,len(string)-1):
            if int(string[j]) - int(string[j+1])!=diff:
                break
        else:
            ans+=1
print(ans)