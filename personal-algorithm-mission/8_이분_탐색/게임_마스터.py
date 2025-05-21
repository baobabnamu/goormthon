import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 만약 추가로 K회를 진행해서 K회의 승리를 거둔다면
# (M + K) * 100 / (N + K)가 그때의 승률이 된다.
# 이때, K가 증가하면 승률은 반드시 증가하기 때문에 단조성을 띈다.
# 그러면 게임을 할 수 있는 횟수가 1회 이상 10^12회 미만이므로
# 그 사이에서 이분 탐색을 통해 목표 승률을 이루는 최소한의 K를 찾으면 된다.

# 현재 승률을 구한다.
cur_rate = M * 100 // N

# 목표 승률은 현재 승률 + 1이다.
goal_rate = cur_rate + 1

# K의 범위
start = 1
end = 999_999_999_999

# 조건을 만족하는 K의 최솟값
res = 1_000_000_000_000

# 이분 탐색
while start <= end:
    mid = (start + end) // 2 # 이 값이 즉 K가 된다.

    rate = (M + mid) * 100 // (N + mid) # K에 따른 승률
    if rate >= goal_rate: # 이 승률이 목표를 달성했다면 현재 K를 기록한다.
        res = mid
        end = mid - 1 # mid보다 큰 값은 고려하지 않아도 된다.
    else:
        start = mid + 1 # mid보다 작은 값은 고려하지 않아도 된다.

# 조건을 만족하는 K가 없었다면 X를 출력한다.
if res == 1_000_000_000_000:
    print('X')
else:
    print(res)