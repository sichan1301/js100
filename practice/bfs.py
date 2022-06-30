from collections import deque

adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1


def bfs():
  dq = deque()
  dq.append(0)
  while dq:
    now = dq.popleft()
    for nxt in range(13):
      if adj[now][nxt]:
        dq.append(nxt)

bfs()