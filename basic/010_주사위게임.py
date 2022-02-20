# 뒤집은 소수

def solution(N):
  res = []
  # l = [list(map(int, input().split())) for _ in range(3)]
  l = [[3,3,6], [2,2,2], [6,2,5]]
  for i in l:
    if len(set(i)) == 1:
      eye = i[0]
      res.append(10000 + eye * 1000)
    elif len(set(i)) == 2:
      eye = max(i, key=i.count)
      res.append(1000 + eye * 100)
    elif len(set(i)) == 3:
      eye = max(i)
      res.append(eye * 100)
  return max(res)

N = 3
print(solution(N))
