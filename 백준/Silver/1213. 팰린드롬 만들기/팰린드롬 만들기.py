import collections

name = input()

alpha = collections.Counter(name)

cnt = 0
center = ''
res = ''
# print(sorted(list(alpha.items())))
for key, value in list(alpha.items()):
    if value % 2 == 1:
        cnt += 1
        center = key
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()
for key, value in sorted(alpha.items()):
    res += (key * (value // 2))

print(res + center + res[::-1])