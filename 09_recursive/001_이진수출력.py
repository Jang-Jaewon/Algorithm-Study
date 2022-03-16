# 이진수 출력
# 풀이1
def solution(N):
  res = ""
  while N > 0:
    N, rest = divmod(N, 2)
    res += str(rest)
  return res[::-1]

# N = int(input())
N = 11
print(solution(N))

# 풀이2
def solution(N, binary):
  N, rest = divmod(N, 2)  
  binary += str(rest)
  if N <= 0:
    return binary[::-1]
  else:
    return solution(N, binary)

# N = int(input())
binary = ""
N = 11
print(solution(N, binary))