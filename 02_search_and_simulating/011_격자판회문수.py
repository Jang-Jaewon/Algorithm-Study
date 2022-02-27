# 격자판 회문수
def solution(l):
  count = 0
  for i in range(3):
    for j in range(7):
      temp = l[j][i:i+5]
      if temp == temp[::-1]:
        count += 1
      for k in range(2):
        if l[i+k][j] != l[i+5-k-1][j]:
          break
      else:
        count += 1
  return count
          
# l =[list(map(int, input().split()))for i in range(7)]
l = [
  [2,4,1,5,3,2,6],
  [3,5,1,8,7,1,7],
  [8,3,2,7,1,3,8],
  [6,1,2,3,2,1,1],
  [1,3,1,3,5,3,2],
  [1,1,2,5,6,5,2],
  [1,2,2,2,2,1,5],
]
print(solution(l)) # 3
