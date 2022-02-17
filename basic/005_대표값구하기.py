def solution(N, l):
  res = -1
  min = float('inf')
  avg_score = round(sum(l) / N)
  for index, value in enumerate(l):
    temp = abs(value - avg_score)
    if temp < min:
      min = temp
      score = value
      res = index+1
    elif temp == min:
      if value > score:
        score = value
        res = index+1
  return avg_score, res

# N = int(input())
# l = list(map(int, input().split()))
N = 10
l = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]
print(solution(N, l))