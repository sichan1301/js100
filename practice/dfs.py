adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1


def dfs(now):
  for nxt in range(13):
    if adj[now][nxt]:
      dfs(nxt)

dfs(0)