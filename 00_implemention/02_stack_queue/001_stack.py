# stack 구현
def stack_push(stack, i):
  stack.append(i)
  return stack

def stack_pop(stack):
  top = stack.pop()
  return top

  
# stack 활용
stack = []
print(stack_push(stack, 5)) # [5]
print(stack_push(stack, 6)) # [5, 6]
print(stack_push(stack, 3)) # [5, 6, 3]
print(stack_push(stack, 1)) # [5, 6, 3, 1]
print(stack_push(stack, 4)) # [5, 6, 3, 1, 4]
print(stack_pop(stack), stack) # 4 [5, 6, 3, 1]
print(stack_pop(stack), stack) # 1 [5, 6, 3]
print(stack_pop(stack), stack) # 3 [5, 6]
print(stack_pop(stack), stack) # 6 [5]
print(stack_pop(stack), stack) # 5 []


# stack 기본 문제(괄호 문제)
def solution(s):
  match = {
    ")" : "(",
    "}" : "{",
    "]" : "[",
  }
  stack = []
  for i in s:
    if len(stack) == 0:
      stack.append(i)
    elif i == '(' or i == '{' or i == '[':
      stack.append(i)
    else:
      temp = stack.pop()
      if temp != match[i]:
        return False
  if len(stack) == 0:
    return True
  else:
    return False

s='{([{}]())}'
print(solution(s))


# class로 stack 구현
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class Stack:
  def __init__(self):
    self.head = None
  
  def push(self, data):
    if self.head == None: # stack이 비어있을 때,
      self.head = Node(data)
    else: # stack이 비어있지 않을 때,
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

  def pop(self):
    if self.head == None: # stack이 비어있을 때,
      return None
    else: # stack이 비어있지 않을 때,
      top = self.head.data
      self.head = self.head.next
      return top

stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")
print(stack.pop()) # D
print(stack.pop()) # C
print(stack.pop()) # B
print(stack.pop()) # A


    