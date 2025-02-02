n = int(input())
if(n==1):
    print(1)
else:
    mod = 10007 # 틀린이유 이거 안했음. 바보
    arr = [0] * (n + 1)
    '''
    규칙
    arr[n-2] 번째  값보다 2^n 승을 더하면 됨
    n은 1씩 증가
    '''
    arr[1] = 1
    arr[2] = 3
    square = 2
    for i in range(1, n - 1):
        arr[i + 2] = arr[i] + pow(2, square)
        square += 1
    print(arr[n]%mod)
