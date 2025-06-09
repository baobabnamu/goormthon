import sys
input = sys.stdin.readline
from collections import deque

# 1번 나라의 언어와 임의로 고른 언어를 이용해 1번 나라에서 시작해 방문할 수 있는 나라의 개수를 구하는 BFS
def bfs(lang):
    dq = deque()
    dq.append(0)
    visited = [False] * N
    visited[0] = True
    while dq:
        i = dq.popleft()
        for j in G[i]:
            if not visited[j] and (a[j] == a[0] or a[j] == lang): # 1번 나라의 언어나 임의로 고른 언어를 사용하는 나라에만 갈 수 있다.
                visited[j] = True
                dq.append(j)

    # 방문한 나라의 개수를 세어 반환한다.
    res = 0
    for i in range(N):
        if visited[i]:
            res += 1
    return res
                

N, M = map(int, input().split())
a = list(map(int, input().split()))

# 그래프 만들기
G = [[] for _ in range(N)]
for _ in range(M):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    G[p].append(q)
    G[q].append(p)

''' 원하는 언어 한 가지를 골라, 1번 나라의 언어를 포함하여 해당하는 언어를 사용하는 나라에만 방문할 수 있다.
이때, 1번 나라에서 출발해 최대한 많은 나라에 방문해야 한다.
이는 1번 나라에서 BFS나 DFS로 탐색을 시작하면 된다.
이때, 어떤 나라에 방문할 수 있는 조건은 그 나라에서 사용하는 언어가 1번 나라의 언어 또는 고른 언어 중 하나여야 한다.
언어는 총 10개 뿐이므로, 1번 나라의 언어를 제외한 총 9개의 언어에 대해 골랐을 때의 최대로 방문할 수 있는 나라의 개수를 전부 구하면 된다. '''

# 1번 나라의 언어가 아닌 언어를 골라 BFS를 시작한다.
ans = 0
for i in range(1, 11):
    if a[0] == i:
        continue
    ans = max(ans, bfs(i))

print(ans)