import math
W, R = map(int, input().split())
print(math.trunc(W * (1 + R / 30)))