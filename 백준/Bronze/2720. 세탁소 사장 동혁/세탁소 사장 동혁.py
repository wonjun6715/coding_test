T = int(input())

coins = [25, 10, 5, 1]

for i in range(T):
    answer = []
    position = 0
    pay = int(input())
    while position != 4:
        answer.append(pay // coins[position])
        pay = pay % coins[position]
        position += 1
    print(*answer)

