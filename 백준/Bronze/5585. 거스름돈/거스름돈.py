n = int(input())

coin = [500, 100, 50, 10, 5, 1]
pay = 1000 - n
cnt = 0
for i in range(len(coin)):
    if coin[i] > pay:
        continue
    cnt += (pay // coin[i])
    pay = pay % coin[i]
print(cnt)
    