# 마구간 정하기
def check_count(mid, l):
  count = 1
  temp = l[0]
  for i in range(1, len(l)):
    if l[i] - temp >= mid:
      count += 1
      temp = l[i]
  return count

def solution(N, C, l):
  res = 0
  left = 1
  right = l[N-1]
  while left <= right:
    mid = (left + right) // 2
    if check_count(mid, l) >= C:
      res = mid
      left = mid + 1
    else:
      right = mid - 1
  return res

# N, C = map(int, input().split())
# l = sorted([int(input() )for _ in range(N)])
N, C = 5, 3
l = [1, 2, 4, 8, 9]
print(solution(N, C, l))
