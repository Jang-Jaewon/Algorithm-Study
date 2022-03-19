# 합이 같은 부분집합(DFS)

# 풀이1
# N = int(input())
# l = list(map(int, input().split()))
N = 6
l = [1, 3, 5, 6, 7, 10]
total = sum(l)
flag = False
def solution(L, sum_val):
  global flag
  if flag:
    return
  if sum_val > (total // 2):
    return
  if L == N:
    if sum_val == (total - sum_val):
      print('YES')
      flag = True
  else:
    solution(L+1, sum_val + l[L])
    solution(L+1, sum_val)
    
solution(0, 0)
if not flag:
  print('NO')

# 풀이2
from itertools import combinations
def solution(N, l):
  target = sum(l) // 2
  for i in range(2, N+1):
    for j in list(combinations(l, i)):
      if sum(j) == target:
        return "YES"
  return 'NO'
  
# N = int(input())
# l = list(map(int, input().split()))
N = 6
l = [1, 3, 5, 6, 7, 10]
print(solution(N, l))