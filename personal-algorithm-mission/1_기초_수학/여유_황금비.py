import sys
input = sys.stdin.readline

T = int(input())

GR = 0

for _ in range(T):
	# A, B 입력 받기
	A, B = map(int, input().split())

	# 비율과 큰 수에 각각 100을 곱하여 계산해야 한다.
	if min(A, B) * 160 <= max(A, B) * 100 <= min(A, B) * 163:
		GR += 1

print(GR)