# 두 리스트 합치기
# 풀이1
def solution(list1, list2):
  sum_list = list1 + list2
  return sorted(sum_list)
n = 3
list1 = [1, 3, 5]
m = 5
list2 = [2, 3, 6, 7, 9]
print(solution(list1, list2))

# 풀이2
def solution(list1, list2, n, m):
  res = []
  p1 = p2 = 0
  while p1 < n and p2 < m:
    if list1[p1] <= list2[p2]:
      res.append(list1[p1])
      p1 += 1
    else:
      res.append(list1[p2])
      p2 += 1
  if p1 < n:
    res = res + list1[p1:]
  elif p2 < m:
    res = res + list2[p2:]
  return res
n = 3
list1 = [1, 3, 5]
m = 5
list2 = [2, 3, 6, 7, 9]
print(solution(list1, list2, n, m))