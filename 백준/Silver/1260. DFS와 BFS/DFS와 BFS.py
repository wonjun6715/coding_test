from collections import deque

def dfs(graph, v, visited):
    visited[v] = True # 방문 처리
    print(v, end = ' ')
    
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # 방문 처리
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True # 방문 처리
        
n,m,v = map(int, input().split())

graph = [[] for _ in range(n + 1)] # 1부터 시작해야하기 때문에 정점의 개수 + 1

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n + 1):
    graph[i].sort()
    
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)


    

