# 후위표현식 만들기(스택)
def solution(data):
  stack = []
  res = ''
  for i in data:
    if i.isdigit():
      res += i
    else:
      if i == '(':
        stack.append(i)
      elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
          res += stack.pop()
        stack.append(i)
      elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
          res += stack.pop()
        stack.append(i)
      elif i == ')':
        while stack and stack[-1] != '(':
          res += stack.pop()
        stack.pop()
  while stack:
    res += stack.pop()
  return res
# data = input()
data = '3+5*2/(7-2)'
print(solution(data))