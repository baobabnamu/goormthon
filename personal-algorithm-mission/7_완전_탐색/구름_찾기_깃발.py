def addFlag(x, y, N, board, dir):
  value = 0

  for dx, dy in dir:
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < N:
      if board[nx][ny] == 1:
        value += 1

  flag[x][y] = value
  
def findK(N, flag, K):
  cnt = 0
  for i in range(N):
    for j in range(N):
      if flag[i][j] == K:
        cnt += 1
  return cnt

dir = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)] # 상화좌우 좌상-우상-우하-좌하

N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
flag = [[0] * N for _ in range(N)]

for i in range(N):
  for j in range(N):
    if board[i][j] != 1:
      addFlag(i, j, N, board, dir)

ans = findK(N, flag, K)

print(ans)