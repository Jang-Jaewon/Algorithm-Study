# 스토쿠 검사

def solution(l):
  for i in range(len(l)):
    low_ch = [0] * 10
    col_ch = [0] * 10
    # print(check_list)
    for j in range(len(l)):
      low_ch[l[i][j]] = 1
      col_ch[l[j][i]] = 1
    if sum(low_ch) != 9 or sum(col_ch) != 9:
      return 'No'
  for i in range(3):
    for j in range(3):
      group_ch = [0] * 10
      for k in range(3):
        for s in range(3):
          group_ch[l[i*3+k][j*3+s]] = 1
      if sum(group_ch) != 9:
        return 'No'
  return 'Yes'

# l = [list(map(int, input().split())) for _ in range(9)]
l = [
  [1, 4, 3, 6, 2, 8, 5, 7, 9], 
  [5, 7, 2, 1, 3, 9, 4, 6, 8], 
  [9, 8, 6, 7, 5, 4, 2, 3, 1],
  [3, 9, 1, 5, 4, 2, 7, 8, 6], 
  [4, 6, 8, 9, 1, 7, 3, 5, 2], 
  [7, 2, 5, 8, 6, 3, 9, 1, 4], 
  [2, 3, 7, 4, 8, 1, 6, 9, 5], 
  [6, 1, 9, 2, 7, 5, 8, 4, 3], 
  [8, 5, 4, 3, 9, 6, 1, 2, 7]
]

print(solution(l)) # Yes