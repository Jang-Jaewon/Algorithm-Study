# 격자판 최대합
def solution(N, ll):
  largest = 0
  for i in range(N):
    sum1 = sum2 = 0
    for j in range(N):
      sum1 += ll[i][j]
      sum2 += ll[j][i]
    largest = max(largest, sum1, sum2)
  sum1 = sum2 = 0  
  for i in range(N):
    sum1 += ll[i][i]
    sum2 += ll[i][N-j-1]
  largest = max(largest, sum1, sum2)
  return largest
    
# N = int(input())
# ll = [list(map(int, input().split())) for _ in range(N)]
N = 5
ll = [
  [10, 13, 10, 12, 15], 
  [12, 39, 30, 23, 11], 
  [11, 25, 50, 53, 15], 
  [19, 27, 29, 37, 27], 
  [19, 13, 30, 13, 19]
]
print(solution(N, ll))
"""
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
"""