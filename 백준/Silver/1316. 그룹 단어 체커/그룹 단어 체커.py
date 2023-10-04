cnt = 0
n = int(input())
tmp = ''
answer = []
for i in range(n):
    tmp = input()
    answer = []
    answer.append(tmp[0])
    for j in range(1, len(tmp)):
        if tmp[j] == tmp[j - 1]:
            continue
        else:
            answer.append(tmp[j])
    if len(set(tmp)) == len(answer):
        cnt += 1
print(cnt)          
            