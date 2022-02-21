# k번째 큰 수
# 풀이1
from itertools import combinations

def solution(n, k, l):
  res = []
  for i in set(combinations(l, 3)):
    res.append(sum(i))
  res = sorted(res, reverse=True)
  return res[k-1]

# n, k = map(int, input("n, k : ").split())
# l = list(map(int, input("l : ").split()))
n, k = 10, 3
l = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]
print(solution(n, k, l))

# 풀이2
def solution(n, k, l):
  res = set()
  for i in range(n):
    for j in range(i+1, n):
      for m in range(j+1, n):
        res.add(l[i]+l[j]+l[m])
  return sorted(res, reverse=True)[k-1]
  

# n, k = map(int, input("n, k : ").split())
# l = list(map(int, input("l : ").split()))
n, k = 10, 3
l = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]
print(solution(n, k, l))
