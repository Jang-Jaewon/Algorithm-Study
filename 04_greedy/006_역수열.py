# 역수열(그리디)
def solution(N, l):
  seq = [0] * N
  for i in range(N):
    for j in range(N):
      if l[i] == 0 and seq[j] == 0:
        seq[j] = i+1
        break
      elif seq[j] == 0:
        l[i] -= 1
  return seq

# N = int(input())
# l = list(map(int, input().split()))  
N = 8
l = [5, 3, 4, 0, 2, 1, 1, 0]
print(solution(N, l))