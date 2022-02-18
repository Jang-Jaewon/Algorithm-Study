# 정다면체
# 풀이1
def solution(N, M):
  d = {}
  res = []
  l = sorted([i+j for i in range(1, N+1) for j in range(1, M+1)])
  for i in l:
    if i not in d:
      d[i] = l.count(i)
  for i in d:
    if d[i] == max(d.values()):
      res.append(i)
  return res

N = 4
M = 6
print(solution(N, M)) # 5 6 7


# 풀이2
def solution(N, M):
  count_l = [0] * (N+M+1)
  for i in range(1, N+1):
    for j in range(1, M+1):
      count_l[i+j] += 1
  max_count = max(count_l)    
  res = [i for i in range(len(count_l)) if count_l[i] == max_count]
  return res

N = 4
M = 6
print(solution(N, M)) # 5 6 7
