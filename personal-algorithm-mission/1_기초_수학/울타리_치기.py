import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

tot = 0 

# 인접한 두 땅에 울타리를 두를 때
# 두 땅 사이의 세로 길이는 두 땅의 세로 방향 길이의 차이가 된다.
for i in range(N - 1):
    tot += abs(A[i] - A[i + 1])

# 가장 왼쪽과 오른쪽에 위치하는 세로 방향의 울타리는 1번, N번 땅의 세로 방향 길이만큼 둘러지게 된다.
tot += A[0]
tot += A[N - 1]

# 아래쪽에 둘러지는 울타리는 땅의 개수만큼 둘러지게 된다.
tot += N

# 위쪽에 둘러지는 울타리의 가로 방향 또한 땅의 개수만큼 둘러지게 된다.
tot += N

print(tot)