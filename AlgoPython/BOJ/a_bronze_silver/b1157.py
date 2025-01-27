# dict = {}
#
# str = list((input().upper()))
#
# for s in str:
#     dict[s] = 0;
# for s in str:
#     dict[s] = dict[s]+1;
#
# max = max(dict.values())
# cnt = 0;
# ans = ""
#
# for _ in dict.keys():
#     if(dict[_]==max):
#         cnt += 1
#         ans = _
#     if(cnt>=2):
#         ans = "?"
#         break;
#
# print(ans)
from collections import Counter

string = input().upper()

counter = Counter(string)

max_count = max(counter.values())
most_common = []

for char, count in counter.items():
    if count == max_count:
        most_common.append(char)

if(len(most_common)==1):
    print(most_common[0])
else:
    print("?")