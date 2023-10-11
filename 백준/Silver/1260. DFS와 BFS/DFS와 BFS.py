from collections import deque
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
n, m, v = map(int, input().split()) # n은 정점의 개수, m은 간선의 개수, v는 시작 지점
 
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):
    graph[i].sort() # 가장 작은 번호부터 방문해야 하므로 정렬
    
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)
