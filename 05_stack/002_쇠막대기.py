# 쇠막대기(스택)
def solution(data):
  stack = []
  cnt = 0
  for i in range(len(data)):
    if data[i] == '(':
      stack.append(data[i])
    else:
      stack.pop()
      if data[i-1] == '(':
        cnt += len(stack)
      else:
        cnt += 1
  return cnt

# data = input()
data = '(((()(()()))(())()))(()())'
print(solution(data))