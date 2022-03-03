# 랜선자르기(결정알고리즘)
# 풀이1
def solution(K, N, l):
  left = 1
  right = max(l)
  while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in l:
      count += i // mid
    if count == N:
      return mid
    elif count < N:
      right = mid - 1
    else:
      left = mid + 1
  return -1
    

# K, N = map(int, input().split())
# l = [int(input()) for _ in range(K)]
K, N = 4, 11
l = [802, 743, 457, 539]
print(solution(K, N, l))

# 풀이2
def line_count(mid, l):
  count = 0
  for i in l:
    count += i // mid
  return count

def solution(K, N, l):
  res = 0
  left = 1
  right = max(l)
  while left <= right:
    mid = (left + right) // 2
    if line_count(mid, l) >= N:
      res = mid
      left = mid + 1
    else:
      right = mid - 1
  return res

# K, N = map(int, input().split())
# l = [int(input()) for _ in range(K)]
K, N = 4, 11
l = [802, 743, 457, 539]
print(solution(K, N, l))