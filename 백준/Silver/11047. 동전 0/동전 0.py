N, K = map(int, input().split())
coins = []
cnt = 0
for i in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)
for i in range(len(coins) - 1, -1, -1):
    cnt += (K // coins[i])
    K = K % coins[i]
print(cnt)
