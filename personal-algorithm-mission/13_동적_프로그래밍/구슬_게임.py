N, M, K = map(int, input().split())
MOD = 100000007
dp = [[0 for _ in range(N + M + 1)] for _ in range(K + 1)]
dp[0][N] = 1

for t in range(K):
    for i in range(1, N + M):
        dp[t + 1][i - 1] = (dp[t + 1][i - 1] + dp[t][i]) % MOD
        dp[t + 1][i] = (dp[t + 1][i] + dp[t][i]) % MOD
        dp[t + 1][i + 1] = (dp[t + 1][i + 1] + dp[t][i]) % MOD
        
ans = 0
for t in range(1, K + 1):
    ans += dp[t][0] + dp[t][N + M]
    ans %= MOD
    
print(ans)