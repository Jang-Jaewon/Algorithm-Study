# 수들의 조합

# 풀이1
# N, M = map(int, input().split())
# array = list(map(int, input().split()))
# target = int(input())
N, K = 5, 3
array = [2, 4, 5, 8, 12]
cnt = 0
target = 6

def solution(level, offset, sum_val):
  global cnt
  if level == K:
    if sum_val % target == 0:
      cnt += 1
  else:
    for i in range(offset, N):
      solution(level+1, i+1, sum_val + array[i])
  return cnt
print(solution(0, 0, 0))

#풀이2
from itertools import combinations

def solution(N, K):
  # array = list(map(int, input().split()))
  # target = int(input())
  array = [2, 4, 5, 8, 12]
  target = 6
  cnt = 0
  for i in combinations(array, K):
    if sum(i) % target == 0:
      cnt += 1
  return cnt

# N, K = map(int, input().split())
N, K = 5, 3
print(solution(N, K))
