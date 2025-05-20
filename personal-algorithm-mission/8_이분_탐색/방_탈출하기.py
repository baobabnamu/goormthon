from bisect import bisect_left

N = int(input())
nums_a = list(map(int, input().split()))
nums_a = sorted(nums_a)

M = int(input())
nums_b = []
for _ in range(M):
    nums_b.append(int(input()))

for num in nums_b:
    # bisect_left는 num이 들어갈 수 있는 가장 왼쪽 위치를 반환
    # 해당 위치의 값이 num과 같다면 num이 존재하는 것
    idx = bisect_left(nums_a, num)
    if idx < N and nums_a[idx] == num:
        print(1)
    else:
        print(0)