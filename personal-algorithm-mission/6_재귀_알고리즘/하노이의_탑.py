import sys
input = sys.stdin.readline

# 하노이의 탑을 해결하는 재귀 함수
# n: 옮겨야 하는 원반의 수, start: n개의 원반이 있는 기둥, end: n개의 원반을 옮겨야 하는 기둥, via: n개의 원반을 start에서 end로 옮기기 위해 거치는 기둥
def hanoi(n, start, end, via):
	# 원반이 하나면 그냥 옮긴다.
	if n == 1:
		moves.append((start, end))
		return

	# n-1개의 원반을 via로 옮긴다.
	hanoi(n - 1, start, via, end)

	# n개의 원반 중 마지막 원반을 end로 옮긴다.
	moves.append((start, end))

	# via로 옮긴 n-1개의 원반을 다시 end로 옮긴다.
	hanoi(n - 1, via, end, start)

# 20개의 원반이 있는 하노이의 탑을 해결하면서
# 그 과정을 차례대로 기록해둔다.

# 원반을 옮기는 과정을 저장해야 한다.
moves = []

# 하노이의 탑
hanoi(20, 1, 3, 2)

K = int(input())

# 저장된 원반을 옮기는 과정을 그대로 구현해서, K번째 이동일 때의 막대마다 원반의 크기의 합을 구하면 된다.

# 막대마다 원반을 저장한다.
sticks = [[] for _ in range(4)]

# 처음엔 20개의 원반 모두 첫 번째 막대에 있다.
for i in range(20, 0, -1):
	sticks[1].append(i)

# 첫 번째 과정부터 K번째 과정까지 그대로 시뮬레이션을 한다
for i in range(K):
	start, end = moves[i]
	# start의 맨 위에 있는 원반을 end로 옮긴다.
	disk = sticks[start].pop()
	sticks[end].append(disk)

# 첫 번째 막대부터 원반의 크기의 합을 구해 출력한다.
for i in range(1, 4):
	print(sum(sticks[i]), end = ' ')
	

# 핵심 아이디어
# 하노이의 탑 문제는 기본적인 재귀문제로, 이에 대한 움직임 과정을 차례대로 리스트에 저장하는 것이 핵심.