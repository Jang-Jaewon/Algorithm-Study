# 후위식 연산(스택)
def solution(data):
  stack = []
  for i in data:
    if i.isdigit():
      stack.append(int(i))
    else:
      if i == '+':
        temp2 = stack.pop()
        temp1 = stack.pop()
        stack.append(temp1 + temp2)
      elif i == '*':
        temp2 = stack.pop()
        temp1 = stack.pop()
        stack.append(temp1 * temp2)
      elif i == '-':
        temp2 = stack.pop()
        temp1 = stack.pop()
        stack.append(temp1 - temp2)
      elif i == '/':
        temp2 = stack.pop()
        temp1 = stack.pop()
        stack.append(temp1 / temp2)
  return stack.pop()
        
# data = input()
data = '352+*9-'
print(solution(data))