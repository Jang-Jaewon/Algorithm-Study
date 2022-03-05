# 창고정리
def solution(L, M, boxs):
  boxs = sorted(boxs)
  for _ in range(M):
    boxs[L-1] -= 1
    boxs[0] += 1
    boxs = sorted(boxs)
  res = boxs[-1] - boxs[0]
  return res
  
# L = int(input())
# boxs = list(map(int, input().split()))
# M = int(input())
L = 10
boxs = [69, 42, 68, 76, 40, 87, 14, 65, 76, 81]
M = 50
print(solution(L, M, boxs))