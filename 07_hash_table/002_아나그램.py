# 아나그램(Anagram)
# 풀이1
def solution(data1, data2):
  res = dict()
  for i in data1:
    res[i] = res.get(i, 0) + 1
  for i in data2:
    if i in res:
      res[i] -= 1
    else:
      return 'NO'
  if all(0 == value for value in res.values()):
    return 'YES'

# data1 = input()
# data2 = input()
data1 = 'AbaAeCe'
data2 = 'baeeACA'
print(solution(data1, data2))

# 풀이2
def solution(data1, data2):
  res1 = dict()
  res2 = dict()
  for i in data1:
    res1[i] = res1.get(i, 0) + 1
  for i in data2:
    res2[i] = res2.get(i, 0) + 1
  for i in res1.keys():
    if i in res2.keys():
      if res1[i] != res2[i]:
        return "NO"
    else:
      return 'NO'
  else:
    return 'YES'

# data1 = input()
# data2 = input()
data1 = 'AbaAeCe'
data2 = 'baeeACA'
print(solution(data1, data2))

# 풀이3
def solution(data1, data2):
  res = dict()
  for i in data1:
    res[i] = res.get(i, 0) + 1
  for i in data2:
    res[i] = res.get(i, 0) - 1
  for i in data1:
    if res.get(i) != 0:
      return 'NO'
  else:
    return 'YES'
  

# data1 = input()
# data2 = input()
data1 = 'AbaAeCe'
data2 = 'baeeACA'
print(solution(data1, data2))

# 풀이4
def solution(data1, data2):
  res1 = [0] * 52
  res2 = [0] * 52
  for i in data1:
    if i.isupper():
      res1[ord(i)-65] += 1
    else:
      res1[ord(i)-71] += 1
  for i in data2:
    if i.isupper():
      res2[ord(i)-65] += 1
    else:
      res2[ord(i)-71] += 1
  for i in range(52):
    if res1[i] != res2[i]:
      return 'NO'
  return 'YES'

# data1 = input()
# data2 = input()
data1 = 'AbaAeCe'
data2 = 'baeeACA'
print(solution(data1, data2))