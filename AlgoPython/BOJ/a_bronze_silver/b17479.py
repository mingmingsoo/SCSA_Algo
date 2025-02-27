'''
문제설명
    일반메뉴 - 그냥 가능
    특별 메뉴- 일반메뉴 총 이만 이상 가능
    서비스 메뉴 - 일+특 총 오만 이상 가능
                & 오직 하나 가능

'''
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
A, B, C = {}, {}, set()
for i in range(a):
    menu, price = input().rstrip().split()
    A[menu] = int(price)
for i in range(b):
    menu, price = input().rstrip().split()
    B[menu] = int(price)
for i in range(c):
    C.add(input().rstrip())

# print(A,B,C)

order_num = int(input())
order_list = [input().rstrip() for i in range(order_num)]

def isOk():
    # 특별 메뉴- 일반메뉴 총 이만 이상 가능
    # 서비스 메뉴 - 일+특 총 오만 이상 가능
    #             & 오직 하나 가능

    A_price = 0 # 일반메뉴 총 가격
    B_price = 0 # 스페셜메뉴 총 가격
    C_count = 0 # 서비스 총 갯수

    for menu in order_list:
        if menu in A:
            A_price += A[menu]
        elif menu in B:
            B_price += B[menu]
        else:
            C_count += 1
    # print(A_price, B_price, C_count)
    if(C_count>1):
        return False
    if(A_price<20000 and B_price>0):
        return False
    if(A_price+B_price <50000 and C_count>0):
        return False
    return True


if(isOk()):
    print("Okay")
else:
    print("No")

