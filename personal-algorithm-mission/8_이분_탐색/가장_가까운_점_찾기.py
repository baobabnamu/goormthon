import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
X = list(map(int, input().split()))

# p와 가장 가까운 점을 찾을 때엔
# 점들을 정렬한 후, p의 좌표 이상이 처음으로 나타나는 점을 이분 탐색으로 찾아서
# 찾은 점과 직전의 점을 p와 비교해서 가장 가까운 점의 좌표를 출력하면 된다.

# 모든 점을 오름차순으로 정렬한다.
X.sort()

for _ in range(Q):
    p = int(input())

    # p의 좌표보다 같거나 크면서, 가장 작은 좌표를 가지는 점을 찾아야 한다.
    start = 0
    end = N - 1
    while start < end:
        mid = (start + end) // 2

        if X[mid] < p: # 현재 점의 좌표가 p의 좌표보다 작다면 조건을 만족하지 않는다.
            start = mid + 1
        else: # p의 좌표보다 같거나 크다면 조건을 만족한다. 그러면 mid보다 더 뒤에 나열된 점들은 고려할 필요가 없어진다.
            end = mid

    # 찾은 점이 첫 번째 점이라면 p의 좌표보다 작은 좌표를 가지는 점은 없기 때문에 찾은 점이 가장 가까운 점이 된다.
    if start == 0:
        print(X[start])

    # p의 좌표보다 같거나 큰 좌표를 가지는 점과 작은 좌표를 가지는 점. 이렇게 두 점 중에서 더 가까운 점을 찾아서 출력하면 된다.
    else:
        if abs(p - X[start - 1]) <= abs(p - X[start]):
            print(X[start - 1])
        else:
            print(X[start])