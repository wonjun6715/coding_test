def dfs(x, y):

    if x < 0 or x >= n or y < 0 or y >= n:
        return False
        # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        graph[x][y] = 0 # 방문 처리
        size = 1 # 현재 덩어리의 크기
        size += dfs(x - 1, y) # 좌
        size += dfs(x + 1, y) # 우
        size += dfs(x, y - 1) # 상
        size += dfs(x, y + 1) # 하
        return size
    return False
        
n = int(input())
graph = []
sizes = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            size = dfs(i, j)
            sizes.append(size)
            result += 1
print(result)
sizes.sort()
for size in sizes:
    print(size)

