# 점수 계산
# 풀이1
def solution(N, l):
  res = [0] * N
  res[0] = l[0]
  for i in range(1, len(l)):
    if l[i] == 1 and l[i-1] == 0:
      res[i] = 1
    elif l[i] == 1 :
      res[i] = res[i-1] + 1
  return sum(res)

N = 10
l = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]
print(solution(N, l)) # 10

# 풀이2
def solution(N, l):
  sum = 0
  cnt = 0
  for i in l:
    if i == 1:
      cnt += 1
      sum += cnt
    else:
      cnt = 0
  return sum

N = 10
l = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]
print(solution(N, l)) # 10