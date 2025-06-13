import sys
input = sys.stdin.readline
from math import ceil, inf
from heapq import heappop, heappush

N, M = map(int, input().split())
S, E, C = map(int, input().split())
S -= 1
E -= 1

G = [[] for _ in range(N)]
for _ in range(M):
	a, b, k = map(int, input().split())
	a -= 1
	b -= 1

	# 이 간선을 지나가는 비용은 C/k의 올림이 된다.
	c = ceil(C / k)
	G[a].append((b, c))
	G[b].append((a, c))

# 다익스트라로 최단 거리를 구한다.
pq = []
heappush(pq, (0, S))
dist = [inf] * N
dist[S] = 0
while pq:
	d, u = heappop(pq)
	if dist[u] < d:
		continue
	for v, w in G[u]:
		if dist[v] > d + w:
			dist[v] = d + w
			heappush(pq, (dist[v], v))

if dist[E] < inf:
	print(dist[E])
else:
	print(-1)