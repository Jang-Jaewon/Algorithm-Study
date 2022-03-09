# queue 구현
from collections import deque
def queue_push(queue, i):
  queue.append(i)
  return queue

def queue_pop(queue):
  front = queue.popleft()
  return front

  
# queue 활용
queue = deque()
print(queue_push(queue, 5)) # deque([5])
print(queue_push(queue, 6)) # deque([5, 6])
print(queue_push(queue, 3)) # deque([5, 6, 3])
print(queue_push(queue, 1)) # deque([5, 6, 3, 1])
print(queue_push(queue, 4)) # deque([5, 6, 3, 1, 4])
print(queue_pop(queue), queue) # 5 deque([6, 3, 1, 4])
print(queue_pop(queue), queue) # 6 deque([3, 1, 4])
print(queue_pop(queue), queue) # 3 deque([1, 4])
print(queue_pop(queue), queue) # 1 deque([4])
print(queue_pop(queue), queue) # 4 deque([])


# queue 기본 문제(요세푸스 문제)
from collections import deque
def solution(n, k):
  res = []
  queue = deque() 
  for i in range(1, n+1):
    queue.append(i)
  while queue:
    for i in range(k-1):
      queue.append(queue.popleft())
    res.append(queue.popleft())
  return res
  
# n, k = map(int, input().split())
n, k = 7, 3
print(solution(n, k)) # [3, 6, 2, 7, 5, 1, 4]


# class로 queue 구현
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
      
  def enqueue(self, data):
    if self.tail == None: # queue가 비어있을 때,
      self.head = self.tail = Node(data)
    else: # queue가 비어있지 않을 때,
      self.tail.next = Node(data)
      self.tail = self.tail.next
      
  def dequeue(self):
    if self.head == None: # queue가 비어있을 때,
      return None
    else: # queue가 비어있지 않을 때,
      front = self.head.data
      self.head = self.head.next
      return front

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.enqueue("D")
print(queue.dequeue()) # A
print(queue.dequeue()) # B
print(queue.dequeue()) # C
print(queue.dequeue()) # D