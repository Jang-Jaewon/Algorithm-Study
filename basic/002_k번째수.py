# k번째 수
def solution():
  n, s, e, k = map(int, input("n, s, e, k : ").split())
  l = list(map(int, input("l : ").split()))
  sorted_l = sorted(l[s-1:e])
  return sorted_l[k-1]

T = int(input("Test Case : "))
for t in range(T):
  print(solution())