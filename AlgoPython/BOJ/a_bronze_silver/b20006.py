player_num, limit = map(int, input().split())

rooms = []

for i in range(player_num):
    level, name = input().split()
    level = int(level)
    if not rooms:
        rooms.append([level, (level, name)])
    else:
        new_room = True
        for room in rooms:
            if len(room) < limit + 1:
                condition = room[0]
                if condition - 10 <= level <= condition + 10:
                    room.append((level, name))
                    new_room = False
                    break
        if new_room:
            rooms.append([level, (level, name)])
for room in rooms:
    room.pop(0)
    room.sort(key=lambda x: x[1])
    if len(room) == limit:
        print("Started!")
    else:
        print("Waiting!")
    for level, name in room:
        print(level, name)
