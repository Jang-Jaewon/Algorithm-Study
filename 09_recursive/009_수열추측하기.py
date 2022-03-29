# 수열 추측하기(파스칼 응용)

#풀이1
# N, final = map(int, input().split())
N, final = 4, 16
p = [0] * N # 순열
b = [1] * N # 이항계수
for i in range(1, N):
  b[i] = b[i-1] * (N-i) // i
check_list = [0] * (N+1)
control = False

def soulution(value, sum_val):
  global control
  if control:
    return
  if value == N and sum_val == final:
    for i in p:
      print(i, end=" ")
      control = True
  else:
    for i in range(1, N+1):
      if check_list[i] == 0:
        check_list[i] = 1
        p[value] = i
        soulution(value+1, sum_val + (p[value] * b[value]))
        check_list[i] = 0

soulution(0, 0)

# 풀이2
from itertools import permutations

def solution(N, final):
  b = [1] * N # 이항계수
  for i in range(1, N):
    b[i] = b[i-1] * (N-i) // i
  array = [i for i in range(1, N+1)]  
  for i in permutations(array):
    sum = 0
    for index, value in enumerate(i):
      sum += (b[index] * value)
    if sum == final:
      return list(i)

# N, final = map(int, input().split())
N, final = 4, 16      
print(solution(N, final))
