# k번째 약수
# 풀이1
def solution(n, k):
  res = []
  for i in range(1, n+1):
    if n % i == 0:
      res.append(i)
  if len(res) <= k-1:
    return -1
  return res[k-1]

n = 6
k = 3
print(solution(n,k))


# 풀이2
def solution(n,k):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
        if count == k:
            return i
    return -1

n = 6
k = 3
print(solution(n,k))    