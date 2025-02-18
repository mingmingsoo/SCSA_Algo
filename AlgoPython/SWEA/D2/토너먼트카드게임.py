T = int(input())
for tc in range(T):
    n = int(input())
    tmp = list(map(int, input().split()))

    arr = []
    for i in range(n):
        arr.append((i + 1, tmp[i]))
    arr.insert(0,0)
    def game(arr,l,r):
        if (l==r):
            return arr[l]

        m = (l+r)//2

        left, right = game(arr,l,m), game(arr,m+1,r)
        player1, player1_show = left
        player2, player2_show = right

        if (player1_show == player2_show):
            if (player1 < player2):
                return left
            else:
                return right
        else:
            if (player1_show == 1 and player2_show == 2) or (player1_show == 2 and player2_show == 3) or (
                    player1_show == 3 and player2_show == 1):
                return right
            else:
                return left


    winner = game(arr,1,n)
    print(f"#{tc+1} {winner[0]}")