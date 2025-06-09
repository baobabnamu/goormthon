import sys
input = sys.stdin.readline
sys.setrecursionlimit(22222)
from math import inf

def dfs1(i, p):
    for j, k in G[i]:
        if j == p:
            continue
        dist[j] = dist[i] + k
        dfs1(j, i)

def dfs2(i, p):
    for j, k in G[i]:
        if j == p:
            continue
        pa[j] = i
        dfs2(j, i)

# 주어지는 그래프는 반드시 트리가 된다.
# 모든 정점까지의 거리의 최댓값이 최소화되는 정점은 트리의 지름 상에 있다.
N = int(input())
G = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    Ai, Li = map(int, input().split())
    G[i].append((Ai, Li))
    G[Ai].append((i, Li))

# 트리의 지름을 이루는 두 정점 u, v를 구한다.
dist = [0] * (N + 1)
dfs1(1, 0)

u = 1
for i in range(2, N + 1):
    if dist[u] < dist[i]:
        u = i

dist = [0] * (N + 1)
dfs1(u, 0)

v = 1
for i in range(2, N + 1):
    if dist[v] < dist[i]:
        v = i

# u를 루트로 한 트리의 정점마다 부모를 구한다.
pa = [0] * (N + 1)
dfs2(u, 0)

# v에서 시작해 u로 거슬러 올라가면서, u까지의 거리와 v까지의 거리를 구해 정답을 갱신해나간다.
res = inf
i = v
while i:
    res = min(res, max(dist[i], dist[v] - dist[i]))
    i = pa[i]

print(res)