# 호준이의 아르바이트
# 풀이1
def solution(array):
  array.sort(reverse=True)
  res = 0
  rank = 1
  for i in range(len(array)-1):
    res += 1
    if array[i] != array[i+1]:
      rank += 1
    if rank > 3:
      return res

# array = list(map(int, input().split()))
array = [97, 86, 75, 66, 55, 97, 85, 97, 97, 95]
print(solution(array))

# 풀이2
def solution(array):
  array.sort(reverse=True)
  cnt = 0
  for i in range(3):
    top = max(array)
    top_cnt = array.count(top)
    cnt += top_cnt
    for _ in range(top_cnt):
      array.remove(top)
  return cnt

# array = list(map(int, input().split()))
array = [97, 86, 75, 66, 55, 97, 85, 97, 97, 95]
print(solution(array))
