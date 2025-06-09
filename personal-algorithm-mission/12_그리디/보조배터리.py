import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
N = int(input())
chargers = [tuple(map(int, input().split())) for _ in range(N)]

''' X 타입, Y 타입 충전기는 각각 A, B에 먼저 할당해야 한다.
이때, 가격이 가장 저렴한 충전기부터 할당한다. '''

# 가격을 기준으로 정렬한다.
chargers.sort()

ct = 0
tot = 0
for ci, ti in chargers:
	if ti == 0: # X 타입 충전기
		if A: # A가 남았다면 A에 할당
			ct += 1
			tot += ci
			A -= 1
		elif C: # C가 남았다면 C에 할당
			ct += 1
			tot += ci
			C -= 1
	else: # Y 타입 충전기
		if B: # B가 남았다면 B에 할당
			ct += 1
			tot += ci
			B -= 1
		elif C: # C가 남았다면 C에 할당
			ct += 1
			tot += ci
			C -= 1

print(ct, tot)