import sys; input = sys.stdin.readline
sys.setrecursionlimit(255555)
MOD = 1000000007

def dfs(i, j):
	# (N, M)에 도착했다면 경로를 하나 찾은 것이다.
	if i == N - 1 and j == M - 1:
		return 1

	# 현재 칸을 이미 방문한 적이 있다면, 현재 칸에서 (N, M)으로 가는 경우의 수가 이미 구해져 있는 상태다.
	if dp[i][j] != -1:
		return dp[i][j]

	# 현재 칸이 방문한 적이 없는 칸이라면, 이 칸에서 (N, M)으로 가는 경우의 수를 구해야 한다.
	dp[i][j] = 0

	for k in range(1, 7):
		# 행의 번호가 증가하는 방향으로 k칸 이동
		if i + k < N and not matrix[i + k][j]: # (i+k+1, j+1)가 격자의 범위 안이어야 하며, 휴식인 칸이 아니어야 한다.
			# 나머지 연산은 분배 법칙이 통한다. 그래서 오버플로우를 방지하기 위해 다음과 같이 분배 법칙을 사용해야 한다.
			# ans = (a + b + ...) % MOD = (a % MOD + b % MOD + ...) % MOD
			dp[i][j] += dfs(i + k, j) # (i+k+1, j+1)에서 (N, M)으로 가는 경우의 수를 더한다.
			dp[i][j] %= MOD
		# 열의 번호가 증가하는 방향으로 k칸 이동
		if j + k < M and matrix[i][j + k] != 1: # (i+1, j+k+1)가 격자의 범위 안이어야 하며, 휴식인 칸이 아니어야 한다.
			dp[i][j] += dfs(i, j + k) # (i+1, j+k+1)에서 (N, M)으로 가는 경우의 수를 더한다.
			dp[i][j] %= MOD

	# 현재 칸에서 (N, M)으로 가는 경우의 수를 반환한다.
	return dp[i][j];

N, M, K = map(int, input().split())

# 휴식인 칸을 행렬에 저장
matrix = [[0] * M for _ in range(N)]
for _ in range(K):
	r, c = map(int, input().split())
	matrix[r - 1][c - 1] = 1

# dp(i, j)를 (i+1, j+1)에서 (N, M)으로 가는 경우의 수로 정의했을 때
# dp(i, j) = dp(i + 1, j) + ... + dp(i + 6, j) + dp(i, j + 1) + ... + dp(i, j + 6)
# (i,j)에서 갈 수 있는 칸들의 경우의 수를 전부 더해주면 된다.
dp = [[-1] * M for _ in range(N)] #  모든 칸에 대한 dp 값을 방문하지 않았다는 의미의 -1로 초기화한다.

print(dfs(0, 0))