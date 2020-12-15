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


def BFS(graph, n, visited):
    queue = deque([n])
    visited[n] = True
    while queue:
        v = queue.popleft()
        print('{}번째 노드'.format(v))
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


BFS(graph, 1, visited)