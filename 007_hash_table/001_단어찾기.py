# 단어 찾기
# 풀이1
def solution(l1, l2):
  res = list(l1-l2)
  return res.pop()
  
# N = int(input())
# l1 = {input() for _ in range(N)}
# l2 = {input() for _ in range(N-1)}
N = 5
l1 = {'big', 'good', 'sky', 'blue', 'mouse'}
l2 = {'big', 'good', 'sky', 'mouse'}
print(solution(l1, l2))

# 풀이2
def solution(N, data):
  for _ in range(N-1):
    word = input()
    data[word] = 0
  for key, value in data.items():
    if value == 1:
      return key
  
# N = int(input())
# data = {input():1 for _ in range(N)}
N = 5
data = {'big': 1, 'good': 1, 'sky': 1, 'blue': 1, 'mouse': 1}
print(solution(N, data))