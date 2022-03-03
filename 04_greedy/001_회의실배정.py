# 회의실 배정
def solution(N, times):
  cnt = 1
  times = sorted(times, key=lambda x : (x[1], x[0]))
  temp = times[0]
  for i in range(1, len(times)):
    if times[i][0] >= temp[1]:
      cnt += 1
      temp = times[i]
  return cnt
# N = int(input())
# times = [list(map(int, input().split())) for i in range(N)]
N = 5
times = [[1, 4], [2, 3], [3, 5], [4, 6], [5, 7]]
print(solution(N, times))