# 1999 = -1임.
# 2000 = 0임.
# 2001 = 1임.
base = 2000

# 음수를 고려한 좌표 생성
matrix = [[0] * 4001 for _ in range(4001)] # 0은 빈칸, 1은 웅덩이

# 초기 좌표 입력 및 base 좌표 변환
current_x, current_y = map(int, input().split())
current_x += base
current_y += base

# 웅덩이 좌표 입력
N = int(input())
for _ in range(N):
  trap_x, trap_y = map(int, input().split())
  matrix[base + trap_x][base + trap_y] = 1

# 명령어 입력
Q = int(input())
commands = list(map(str, input().split()))

for idx in range(Q):
  command = commands[idx]
  if command == "L" and matrix[current_x-1][current_y] != 1:
    current_x -= 1
  elif command == "R" and matrix[current_x+1][current_y] != 1:
    current_x += 1
  elif command == "U" and matrix[current_x][current_y+1] != 1:
    current_y += 1
  elif command == "D" and matrix[current_x][current_y-1] != 1:
    current_y -= 1

# 최종 좌표 출력
print(current_x-base, current_y-base)