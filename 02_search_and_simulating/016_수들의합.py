# 수들의 합
def solution(N,M,l):
  cnt = 0
  for i in range(len(l)):
    for j in range(i+1, len(l)+1):
      if sum(l[i:j]) == M:
        cnt += 1
      elif sum(l[i:j]) > M:
        break
  return cnt
N, M = 8, 3
l = [1, 2, 1, 3, 1, 1, 1, 2]
print(solution(N,M,l))