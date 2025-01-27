
def isGroup(word):
    string = word[0]

    for i in range(1, len(word)):
        if (word[i] != word[i - 1]):
            string += word[i]  # 중복 제거

    sett = set(string)

    if (len(sett) != len(string)):
        return False
    return True


T = int(input())
ans = 0

for t in range(T):
    if (isGroup(input())):
        ans += 1
print(ans)
