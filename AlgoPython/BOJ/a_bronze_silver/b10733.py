'''
문제설명
    재현이가 잘못부를 때마다 0을 외쳐서 쓴 수를 지움
    안지워진 수들의 합?

입력
    0일경우 지움, empty 상관 안써도됨
'''
n = int(input())
stk = []
for i in range(n):
    num = int(input())
    if num==0:
        stk.pop()
    else:
        stk.append(num)

print(sum(stk))