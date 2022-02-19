# 에라토스테네스의 체(소수 문제)

# 풀이1
def solution(N):
  check_list = [0] * (N+1)
  cnt = 0
  for i in range(2, N+1):
    if check_list[i] == 0:
      cnt += 1
      for j in range(i, N+1, i):
        check_list[j] = 1
  return cnt

N = 20
print(solution(N))


# 풀이2
def solution(N):
  check_list = [True] * (N+1)
  m = int(N ** 0.5)
  for i in range(2, m+1):
    if check_list[i] == True:
      for j in range(i+i, N+1, i):
        check_list[j] = False
  res = [i for i in range(2, N+1) if check_list[i] == True]
  print(check_list)
  print(res)
  return len(res)

N = 20
print(solution(N))