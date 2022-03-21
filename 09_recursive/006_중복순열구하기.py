# 중복순열구하기
# 풀이1
# N, M = map(int, input().split())
N, M = 3, 2
res = [0] * M
cnt = 0
def solution(i):
  global cnt
  if i == M:
    print(res)
    cnt += 1
    return
  else:
    for j in range(1, N+1): # 1,2,3
      res[i] = j
      solution(i+1)
  return cnt

print(solution(0))

# 풀이2
def solution(N, M):
  for i in range(1, N+1):
    for j in range(1, N+1):
      print(i, j)
# N, M = map(int, input().split())
N, M = 3, 2
solution(N, M)