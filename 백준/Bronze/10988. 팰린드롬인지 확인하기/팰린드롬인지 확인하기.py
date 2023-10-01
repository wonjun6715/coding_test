word = input()
flag = 0
for i in range(len(word) // 2):
    if word[i] == word[len(word) - i - 1]:
        continue
    else:
        print(0)
        flag = 1
        break
if flag != 1:
    print(1)