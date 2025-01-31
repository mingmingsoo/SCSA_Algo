# n = int(input())
# stack = []
# idx = 1
# ans = []
# for i in range(n):
#     num = int(input())
#     while (idx <= num):
#         stack.append(idx)
#         idx += 1
#         ans.append("+")
#     while(stack and stack[-1]!=num):
#         stack.pop()
#         ans.append("-")
#     if(not stack):
#         ans = "NO"
#         break
#     elif(stack[-1]==num):
#         stack.pop()
#         ans.append("-")
# if(ans =="NO"):
#     print(ans)
# else:
#     for x in ans:
#         print(x)
N = int(input())
lst = [int(input()) for _ in range(N)]

ans = []
stk = []
num = 1

for n in lst:
    # [1] n을 스택에서 꺼내려면 push되어 있어야 함
    while num<=n:
        stk.append(num)
        num+=1
        ans.append('+')

    # [2] 스택에서 pop해서 n을 만들수 있으면 pop 아니면 NO
    if stk[-1]==n:
        stk.pop()
        ans.append('-')
    else:
        ans = 'NO'
        break
if ans == 'NO':
    print(ans)
else:
    print(*ans, sep='\n')