# 곶감(모래시계)
def change_ll(M, l):
  for i in range(M):
    h, v, s = map(int, input().split())
    if v == 0:
      for i in range(s):
        l[h-1].append(l[h-1].pop(0))
    else:
      for i in range(s):
        l[h-1].insert(0, l[h-1].pop())
  return l
  
def solution(N,ll):
  res = 0
  start, end = 0, N
  for i in range(N):
    for j in range(start, end):
      res += ll[i][j]
    if i < N // 2:
      start += 1
      end -= 1
    else:
      start -= 1
      end += 1
  return res
# N = int(input()) 
# ll = [list(map(int, input().split())) for _ in range(N)]
# M = int(input())
N = 5
l = [
  [10, 13, 10, 12, 15],
  [12, 39, 30, 23, 11],
  [11, 25, 50, 53, 15],
  [19, 27, 29, 37, 27],
  [19, 13, 30, 13, 19],
] 
M = 3
ll = change_ll(M, l)
print(solution(N,ll))
"""
2 0 3
5 1 2
3 1 4
"""