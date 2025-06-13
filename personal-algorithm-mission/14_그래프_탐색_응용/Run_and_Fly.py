import sys
input = sys.stdin.readline
from math import inf
from collections import deque
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

def f(K):
    # dist(i, j, k): (i,j) 위치에 에너지가 k만큼 남은 상태로 도달하기 위한 최단 거리
    dist = [[[inf] * (K + 1) for _ in range(M)] for _ in range(N)]

    # bfs
    dq = deque([(0, 0, K)])
    dist[0][0][K] = 0
    while dq:
        i, j, k = dq.popleft()

        # rest
        if k < K and S[i][j] == 2 and dist[i][j][k + 1] > dist[i][j][k] + 1:
            dist[i][j][k + 1] = dist[i][j][k] + 1
            dq.append((i, j, k + 1))

        for di, dj in dir:
            ni = i + di; nj = j + dj

            # 다음 위치가 유효한 위치인지 확인
            if not (0 <= ni < N and 0 <= nj < M) or S[ni][nj] == 0:
                continue

            # run
            if S[i][j] == 2 and S[ni][nj] == 2:
                if dist[ni][nj][k] > dist[i][j][k] + 1:
                    dist[ni][nj][k] = dist[i][j][k] + 1
                    dq.append((ni, nj, k))

            # fly
            else:
                if k > 0 and dist[ni][nj][k - 1] > dist[i][j][k] + 1:
                    dist[ni][nj][k - 1] = dist[i][j][k] + 1
                    dq.append((ni, nj, k - 1))

    # (N-1,M-1)에 T 이내로 도달한 상태가 있는지 확인
    for k in range(K + 1):
        if dist[N - 1][M - 1][k] <= T:
            return True
    return False

N, M, T = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]

''' 처음부터 계속 날면서 모든 칸을 방문하고 탈출구로 도달할 때의 필요한 에너지는 N*M-1이다.
그럼 [0, N*M-1] 범위에서 K의 최솟값을 찾으면 된다.
f(K)를 최대 에너지가 K일 때의 T초 이내에 도달 가능하면 1, 불가능하면 0인 함수라고 정의한다면, 이분 탐색을 쓸 수 있는 함수 꼴이 된다.
그러므로 범위 내에서 이분 탐색을 이용해서 f(K)=1인 K 중에서 최솟값을 찾으면 된다. '''

st = 0; en = N * M - 1
ans = -1
while st <= en:
    mid = (st + en) >> 1
    if f(mid):
        ans = mid
        en = mid - 1
    else:
        st = mid + 1

print(ans)