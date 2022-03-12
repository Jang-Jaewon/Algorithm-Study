# 교육과정 설계
from collections import deque

def solution(rule, N, l):
  res = []
  for i in l:
    queue = deque(rule)
    for j in i:
      if j in queue:
        if j != queue.popleft():
          res.append('NO')
          break
    else:
      if len(queue) == 0:
        res.append('YES')
      else:
        res.append('NO')
  return res
  
# rule = input()
# N = int(input())
# l = [input() for _ in range(N)]
rule = 'CBA'
N = 3
l = ['CBDAGE', 'FGCDAB', 'CTSBDEA']
print(solution(rule, N, l))
