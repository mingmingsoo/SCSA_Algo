n, b = map(int,input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

def mul(arr1, arr2):
    square_arr = [[0] * n for i in range(n)]

    for x in range(n):
        for y in range(n):
            for i in range(n):
                square_arr[x][y] += (arr1[x][i] * arr2[i][y])%1000
    return square_arr

def my_pow(arr, b):
    if(b==1):
        return arr

    if(b%2==0):
        tmp = my_pow(arr,b//2)
        return mul(tmp,tmp)
    elif(b%2==1):
        tmp = my_pow(arr,(b-1)//2)
        return mul(mul(tmp,tmp),arr)


ans_arr =my_pow(arr,b)
for i in range(n):
    for j in range(n):
        print(ans_arr[i][j]%1000, end = " ")
    print()



