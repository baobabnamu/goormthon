import sys
input = sys.stdin.readline
MOD = 1000000007

N = int(input())

# 피보나치 수열의 i번째 항을 dp(i)라 할 때,
# 정의에 의해서 dp(i) = dp(i - 1) + dp(i - 2)가 된다.
# 이는 dp로 해결할 수 있는 점화식이다.

# 첫 두 항은 0, 1이다.
if N <= 2:
	print(N - 1)
	exit()

# dp 배열을 크기가 N이 되게 초기화해서
# 세 번째 항부터 채워간다.
dp = [0] * N
dp[1] = 1
for i in range(2, N):
	dp[i] = (dp[i - 1] + dp[i - 2]) % MOD # 나머지 분배 법칙을 이용해서 오버플로우를 방지한다.

print(dp[N - 1])