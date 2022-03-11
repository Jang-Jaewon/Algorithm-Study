# Linked List
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class NodeMgmt:
  def __init__(self, data):
    self.head = Node(data)

  def add(self, data):
    if self.head == None: # self.head 없음(data가 처음 추가됬을 때)
      self.head = Node(data)
    else: # self.head 존재
      node = self.head
      while node.next:
        node = node.next
      node.next = Node(data)

  def search(self, data):
    node = self.head
    while node:
      if node.data == data:
        return node
      else:
        node = node.next
    print('Does Not Exist')

  def insert(self, index, data):
    node = self.head
    for i in range(index-1):
      node = node.next
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node
    
  def delete(self, data):
    if self.head == None:
      print('Does Not Exist')
      return
    if self.head.data == data: # 삭제할 Node가 self.head일 때,
      temp = self.head
      self.head = self.head.next
      del temp
    else: # 삭제할 Node가 중간이나 맨 끝에 있을 때,
      node = self.head
      while node.next:
        if node.next.data == data:
          temp = node.next
          node.next = node.next.next
          del temp
        else:
          node = node.next
      
  def desc(self):
    node = self.head
    res = []
    while node:
      res.append(node.data)
      node = node.next
    print(res)


# Node 생성
linked_list = NodeMgmt(0)
linked_list.desc() # [0]

# Node 추가
for i in range(1, 10):
  linked_list.add(i)
linked_list.desc() # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Node 탐색
linked_list.search(100) # Does Not Exist

# Node 삽입
linked_list.insert(3, 2.5) 
linked_list.desc() # [0, 1, 2, 2.5, 3, 4, 5, 6, 7, 8, 9]

# Node 삭제
linked_list.delete(0)
linked_list.delete(2.5)
linked_list.desc() # [1, 2, 3, 4, 5, 6, 7, 8, 9]