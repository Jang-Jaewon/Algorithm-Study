# 문자열 압축하기

# data = input()
def solution(data):
  res = []
  for i in range(len(data) - 1):
      if data[i] != data[i + 1]:
          res.append(data[i])
          res.append(str(data.count(data[i])))
  return "".join(res)
  
data = "aaabbbbcdddd"
print(solution(data)) # a3b4c1