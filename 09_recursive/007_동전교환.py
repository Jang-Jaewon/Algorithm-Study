# 동전교환

# N = int(input())
# l = list(map(int, input().split()))
# M = int(input())
N = 3
l = [1, 2, 5]
l.sort(reverse=True)
M = 15
res = 99999

def solution(i, sum_val):
  global res
  if i > res:
    return
  if sum_val > M:
    return
  if sum_val == M:
    if i < res:
      res = i
  else:
    for j in range(N):
      solution(i+1, sum_val + l[j])
  return res
      
print(solution(0, 0))