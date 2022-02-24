# 사과나무(다이아몬드)
def solution(N,ll):
  res = 0
  start = end = N // 2
  for i in range(N):
    for j in range(start, end+1):
      res += ll[i][j]
    if i < N // 2:
      start -= 1
      end += 1
    else:
      start += 1
      end -= 1
  return res
  
# N = int(input()) 
# ll = [list(map(int, input().split())) for _ in range(N)]
N = 5
ll = [
  [10, 13, 10, 12, 15],
  [12, 39, 30, 23, 11],
  [11, 25, 50, 53, 15],
  [19, 27, 29, 37, 27],
  [19, 13, 30, 13, 19],
] 

print(solution(N,ll))
