# 회문 문자열 검사
# 풀이1
def solution(l):
  res = []
  reverse_l = [i[::-1] for i in l]
  for i in range(len(l)):
    if l[i] == reverse_l[i]:
      res.append('YES')
    else: 
      res.append('NO')
  return res

# N = int(input())
# l = [input().upper() for _ in range(N)]
N = 5
l = ['level', 'moon', 'abcba', 'soon', 'gooG']
answer = solution(l)
for i in range(len(answer)):
  print(f"#{i+1} {answer[i]}")

# 풀이2
def solution(s):
  s = s.upper()
  size = len(s)
  for i in range(size//2):
    if s[i] != s[-i-1]:
      return "NO"
      break
    else:
      return "YES"

# N = int(input())
N = 5
for i in range(N):
  s = input()
  print(f"#{i+1} {solution(s)}")