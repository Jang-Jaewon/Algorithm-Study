# 응급실(큐)
from collections import deque

# 풀이1
def solution(N, M, l):
  l = [(idx, value) for idx, value in enumerate(l)]
  queue = deque(l)
  target = queue[M]
  res = 0
  while True:
    priority = max(queue, key= lambda x: x[1])
    current = queue.popleft()
    if priority != current:
      queue.append(current)
    else:
      res += 1
      if current == target:
        return res

# N, M = map(int, input().split())
# l = list(map(int, input().split()))
# N, M = 5, 2
# l = [60, 50, 70, 80, 90]
N, M = 6, 0
l = [60, 60, 90, 60, 60, 60]
print(solution(N, M, l)) # 5

# 풀이2
def solution(N, M, l):
  l = [(idx, value) for idx, value in enumerate(l)]
  queue = deque(l)
  res = 0
  while True:
    current = queue.popleft()
    if any(current[1] < i[1] for i in queue):
      queue.append(current)
    else:
      res += 1
      if current[0] == M:
        return res

# N, M = map(int, input().split())
# l = list(map(int, input().split()))
N, M = 6, 0
l = [60, 60, 90, 60, 60, 60]
print(solution(N, M, l)) # 5