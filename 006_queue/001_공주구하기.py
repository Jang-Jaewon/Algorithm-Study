# 공주 구하기(큐)

from collections import deque

def solution(N, K):
  res = []
  queue = [i for i in range(1, N+1)]
  queue = deque(queue)
  while queue:
    for _ in range(K-1):
      queue.append(queue.popleft())
    res.append(queue.popleft())
  return res[-1]

# N, K = map(int, input().split())
N, K = 8, 3
print(solution(N, K))