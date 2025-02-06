N = int(input())

left = [0]*(N+1)
right = [0]*(N+1)

for i in range(1,N+1):
    tmp = list(map(lambda x: ord(x)-64, input().split()))
    num = tmp[0]
    if(tmp[1]!=-18): # "."
        left[num] = tmp[1]
    if (tmp[2] != -18):
        right[num] = tmp[2]

def preord(n):
    # root left right
    if(n <1):
        return
    pre_word.append(n)
    preord(left[n])
    preord(right[n])


pre_word = []
preord(1)
for x in pre_word:
    print(chr(x+64),end = "")
print()
def inord(n):
    # left root right
    if (n < 1):
        return
    inord(left[n])
    in_word.append(n)
    inord(right[n])

in_word = []
inord(1)
for x in in_word:
    print(chr(x+64),end = "")
print()
def postord(n):
    if (n < 1):
        return
    postord(left[n])
    postord(right[n])
    post_word.append(n)

post_word = []
postord(1)
for x in post_word:
    print(chr(x+64),end = "")