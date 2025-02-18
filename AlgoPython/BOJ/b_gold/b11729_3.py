n = int(input())
print(2**n-1)
def hanoi(n,start,middle,end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1,start,end,middle)
    print(start,end)
    hanoi(n-1,middle,start,end)

hanoi(n,1,2,3)