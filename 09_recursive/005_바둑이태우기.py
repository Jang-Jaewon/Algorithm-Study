# 바둑이 태우기

# 풀이1
C, N = 259, 5
l = [81, 58, 42, 33, 61]
res = 0
def solution(i, sum_val):
  global res
  if sum_val > C:
    return
  if i == N:
    if sum_val >= res:
      res = sum_val
  else:
      solution(i+1, sum_val + l[i])
      solution(i+1, sum_val)
  return res
    
print(solution(0, 0))

# 풀이2 
from itertools import combinations

def solution(C, N, l):
  res = []
  for i in range(2, N+1):
    for j in list(combinations(l, i)):
      if sum(j) <= C:
        res.append(sum(j))
  return max(res)

C, N = 259, 5
l = [81, 58, 42, 33, 61]
print(solution(C, N, l))
