# 뮤직비디오(결정알고리즘)
def check_size(mid, l):
  count = 1
  sum = 0
  for i in l:
    if sum + i > mid:
      count += 1
      sum = i
    else:
      sum += i
  return count

def solution(N, M, l):
  left = 1
  right = sum(l)
  res = 0
  while left <= right:
    mid = (left + right) // 2
    if mid >= max(l) and check_size(mid, l) <= M:
      res = mid
      right = mid - 1
    else:
      left = mid + 1
  return res

# N, M = map(int, input().split())
# l = list(map(int, input().split()))
N, M = 9, 3
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(solution(N, M, l))
