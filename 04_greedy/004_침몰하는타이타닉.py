# 침몰하는 타이타닉
# 풀이1
def solution(N, M, l):
  cnt = 0
  l = sorted(l)
  while l:
    if len(l) == 1:
      cnt += 1
      break
    if l[0] + l[-1] <= M:
      l.pop()
      l.pop(0)
      cnt += 1
    else:
      l.pop()
      cnt += 1
  return cnt
  
# N, M = map(int, input().split())
# l = list(map(int, input().split()))
N, M = 5, 140
l = [90, 50, 70, 100, 60]
print(solution(N, M, l))

# 풀이2
from collections import deque

def solution(N, M, l):
  cnt = 0
  l = deque(sorted(l))
  while l:
    if len(l) == 1:
      cnt += 1
      break
    if l[0] + l[-1] <= M:
      l.pop()
      l.popleft()
      cnt += 1
    else:
      l.pop()
      cnt += 1
  return cnt
  
# N, M = map(int, input().split())
# l = list(map(int, input().split()))
N, M = 5, 140
l = [90, 50, 70, 100, 60]
print(solution(N, M, l))