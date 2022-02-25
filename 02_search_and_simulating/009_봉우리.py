# 봉우리 문제
def cover_zero(N, l):
  l.insert(0, [0] * N)
  l.append([0] * N)
  for i in l:
    i.insert(0,0)
    i.append(0)
  return l
    
def solution(N, ll):
  cnt = 0
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  for i in range(1, N+1):
    for j in range(1, N+1):
      if all(ll[i][j] > ll[i+dx[k]][j+dy[k]] for k in range(4)):
        cnt += 1
  return cnt
        
# N = int(input()) 
# l = [list(map(int, input().split())) for _ in range(N)]
N = 5
l = [
  [5, 3, 7, 2, 3],
  [3, 7, 1, 6, 1],
  [7, 2, 5, 3, 4],
  [4, 3, 6, 4, 1],
  [8, 7, 3, 5, 2],
] 
ll = cover_zero(N, l)
print(solution(N,ll))

