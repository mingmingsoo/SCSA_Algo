# def dfs(n):
#     if (n == 0):
#         return
#     dfs(n - 1)
#     print(n, end=" ")
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     print(f"#{tc + 1}", end = " ")
#
#     dfs(n)
#     print()
#


# def dfs(n):
#     if (n == 0):
#         return
#     print(n, end=" ")
#     dfs(n - 1) # 전 문제와 위 아래 순서만 바꾸면 된다.
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     print(f"#{tc + 1}", end = " ")
#
#     dfs(n)
#     print()

# def dfs(n):
#     global ans
#     if (n == 0):
#         return
#     ans += n
#     dfs(n - 1)
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     print(f"#{tc + 1}", end = " ")
#     ans = 0
#     dfs(n)
#     print(ans,end="")
#     print()




# def dfs(n):
#     global ans
#     if (n == 1):
#         return
#     ans *= n
#     dfs(n - 1)
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     print(f"#{tc + 1}", end = " ")
#     ans = 1
#     dfs(n)
#     print(ans,end="")
#     print()


# def dfs(n):
#     global ans
#     if (n == 2):
#         return # 종료조건
#
#     dfs(n-1) # 재귀
#     ans[n] = ans[n-1]+ans[n-2] # 단위작업
#
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     ans = [0]*(n+1)
#     ans[1]=1
#     ans[2]=1
#
#     print(f"#{tc + 1}", end = " ")
#     dfs(n)
#     print(ans[n])


# def dfs(n):
#     global ans
#     if (n == 2):
#         return # 종료조건
#
#     dfs(n-1) # 재귀
#     ans[n] = ans[n-1]+ans[n//2] # 단위작업
#
#
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     ans = [0]*(n+1)
#     ans[1]=1
#     ans[2]=2
#
#     print(f"#{tc + 1}", end = " ")
#     dfs(n)
#     print(ans[n])


# def dfs(n):
#     global ans
#     if (n < 0):
#         return # 종료조건
#
#     dfs(n-1) # 재귀
#     ans+=arr[n] # 단위작업
#
#
# T = int(input())
# for tc in range(T):
#     arr = list(map(int, list(input())))
#     print(arr)
#     ans = 0
#     print(f"#{tc + 1}", end = " ")
#     dfs(len(arr)-1)
#     print(ans)

'''
left = [~~]
right = [~~]
def inord(n):
    if n>0:
        inord(left[n])
        print(n)
        inord(right[n])
'''
