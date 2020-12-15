from collections import deque

graph = [[], [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6],
         [1, 7]]

visited = [False] * 9


def DFS(graph, n, visited):
    visited[n] = True
    print('{}번 노드 방문'.format(n))
    for i in graph[n]:
        if not visited[i]:
            DFS(graph, i, visited)


DFS(graph, 1, visited)

for i in range(len(visited)):
  visited[i] = False




queue = deque()
queue.append(1)
visited[1] = True
def BFS(graph,visited):

  if not queue:
    return
  v = queue.popleft()
  print('{}번째 노드 방문'.format(v))

  for i in graph[v]:
    if not visited[i]:
      queue.append(i)
      visited[i] = True
  BFS(graph,visited)


BFS(graph,visited)
