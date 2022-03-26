# 조합 구하기

# 풀이1
# N, M = map(int, input().split())
N, M = 4, 2
res = [0] * M
cnt = 0
def solution(value, start):
  global cnt
  if value == M:
    for i in range(M):
      print(res[i], end=" ")
    print()
    cnt += 1
  else:
    for i in range(start, N+1):
      res[value] = i
      solution(value+1, i+1)
  return cnt

solution(0, 1)

# 풀이2
from itertools import combinations
N, M = 4, 2
def solution(N, M):
  l = list(combinations(range(1, N+1), M))
  return l
print(solution(N, M))