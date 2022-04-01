def solution(data):
  stack = []
  # if data.count('(') != data.count(')'):
  #   return False
  for i in data:
    if i == '(':
      stack.append(i)
    else:
      if len(stack) == 0:
        return False
      stack.pop()
  if len(stack) == 0:
    return True
  else:
    return False

  
# data = inut()
data = '(((()())()))'
print(solution(data))