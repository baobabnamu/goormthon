import sys
input = sys.stdin.readline

N = int(input())
C = list(map(int, input().split()))

# dp(i): j<=i인 j번 동전부터 i번 동전까지 주웠을 때의 최적값이라 정의한다.
# dp(i) = max(dp(i - 1), 0) + c(i)가 된다. i-1번 동전까지 줍고 연속으로 i번 동전을 줍거나, i번 동전부터 새로 줍거나 둘 중 하나이다.	
dp = [0] * N
dp[0] = C[0]
for i in range(1, N):
	dp[i] = max(dp[i - 1], 0) + C[i]

# 모든 i에 대한 dp 값 중에서 최댓값이 정답이 된다. 즉, 어느 동전까지 주운 것이 최적인지 확인해야 한다.
ans = 0 # 아무 동전도 줍지 않을 때엔 0이다.
for i in range(N):
	ans = max(ans, dp[i])

print(ans)