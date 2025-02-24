order_list = []
for i in range(36):
    order_list.append(input())
visited = [[False] * 6 for i in range(6)]
order_list.append(order_list[0])
def game():
    for i in range(36):
        before = order_list[i]
        after = order_list[i + 1]
        x1, y1, x2, y2 = ord(before[0]) - 65, int(before[1]) - 1, ord(after[0]) - 65, int(after[1]) - 1
        if visited[x1][y1]:
            print("Invalid")
            return
        visited[x1][y1] = True

        if (abs(x2 - x1), abs(y2 - y1)) not in {(1, 2), (2, 1)}:
            print("Invalid")
            return

    print("Valid")

game()
