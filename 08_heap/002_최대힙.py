# 최대힙
import heapq

def solution():
  res = []
  l = []
  while True:
    num = int(input())
    if num == -1:
      return res
    if num  == 0:
      if len(l) == 0:
        res.append(-1)
      else:
        res.append(-heapq.heappop(l))
    else:
      heapq.heappush(l, -num)
    # print(f"l:{l}, res:{res}")
      
print(solution())