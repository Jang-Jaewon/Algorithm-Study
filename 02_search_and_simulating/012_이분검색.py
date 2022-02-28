# 이분검색
def solution(N, M, l):
  l = sorted(l)
  left = 0
  right = N - 1
  while left <= right:
    mid = (left + right) // 2
    if l[mid] == M:
      return mid + 1
    elif l[mid] < M:
      left = mid + 1
    else:
      right = mid - 1
  return -1
          
# N, M = map(int, input().split())
# l = list(map(int, input().split()))
N, M = 8, 32
l = [23, 87, 65, 12, 57, 32, 99, 81]
print(solution(N, M, l))