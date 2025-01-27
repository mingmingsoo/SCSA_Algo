string = input()
time = 0

for s in string:
    if (65 <= ord(s) <= 67):
        time += 3
    elif (68 <= ord(s) <= 70):
        time += 4
    elif (71 <= ord(s) <= 73):
        time += 5
    elif (74 <= ord(s) <= 76):
        time += 6
    elif (77 <= ord(s) <= 79):
        time += 7
    elif (80 <= ord(s) <= 83): # 4
        time += 8
    elif (84 <= ord(s) <= 86):
        time += 9
    elif (87 <= ord(s)):
        time += 10
print(time)
