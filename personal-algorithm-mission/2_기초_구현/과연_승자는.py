N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_score = 0
B_score = 0

for i in range(len(A)):
  if A[i] > B[i]:
    if A[i] - B[i] == 7:
      A_score -= 1
      B_score += 3
    else:
      A_score += 2
  elif A[i] < B[i]:
    if B[i] - A[i] == 7:
      A_score += 3
      B_score -= 1
    else:
      B_score += 2
  elif A[i] == B[i]:
    A_score += 1
    B_score += 1

print(A_score, B_score)