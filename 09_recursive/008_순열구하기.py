# 순열구하기
# 풀이1

# N, M = map(int, input().split())
N, M = 3, 2
check_list = [0] * (N+1)
res = [0] * N
cnt = 0
def solution(i):
  global cnt
  if i == M:
    for j in range(i):
      print(res[j], end=" ")
    print()
    cnt += 1
  else:
    for j in range(1, N+1):
      if check_list[j] == 0:
        check_list[j] = 1
        res[i] = j
        solution(i+1)
        check_list[j] = 0
  return cnt

print(solution(0))

# 풀이2
from itertools import permutations

def solution(N, M):
  l = [i for i in range(1, N+1)]
  res = list(permutations(l, M))
  for i in res:
    print(i[0], i[1])
  print(len(res))
# N, M = map(int, input().split())
N, M = 3, 2
solution(N, M)