# 증가수열 만들기
def solution(N, l):
  lt = 0
  rt = N-1
  last = 0
  res = ""
  temp = []
  while lt <= rt:
    if l[lt] > last:
      temp.append((l[lt], 'L'))
    if l[rt] > last:
      temp.append((l[rt], 'R'))
    temp.sort()
    if len(temp) == 0: 
      break
    else:
      res += temp[0][1]
      last = temp[0][0]
      if temp[0][1] == 'L':
        lt += 1
      else:
        rt -= 1
    temp.clear()
  return res
  
# N = int(input())
# l = list(map(int, input().split()))
N = 5
l = [2, 4, 5, 1, 3]
print(len(solution(N, l)))
print(solution(N, l))