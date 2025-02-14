n = int(input())
# print(int(n**(0.5)))


start = 1
end = n//2+1 # 1일때를 위해서

while start<=end:
    middle = (start+end)//2

    if middle*middle == n:
        print(middle)
        break
    elif middle*middle < n:
        start = middle+1
    else:
        end = middle -1