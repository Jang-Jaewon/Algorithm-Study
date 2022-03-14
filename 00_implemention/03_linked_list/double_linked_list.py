class Node:
  def __init__(self, data, prev=None, next=None):
    self.data = data
    self.prev = prev
    self.next = next

class NodeMgmt:
  def __init__(self, data):
    self.head = Node(data)
    self.tail = self.head

  def insert(self, data):
    if self.head == None:
      self.head = Node(data)
      self.tail = self.head
    else:
      node = self.head
      while node.next:
        node = node.next
      new_node = Node(data)
      node.next = new_node
      new_node.prev = node
      self.tail = new_node

  def search_from_head(self, data):
    if self.head == None:
      return False
    node = self.head
    while node:
      if node.data == data:
        return node
      else:
        node = node.next
    print('Does Not Exist')
    
  def search_from_tail(self, data):
    if self.tail == None:
      return False
    node = self.tail
    while node:
      if node.data == data:
        return node
      else:
        node = node.prev
    print('Does Not Exist')

  def insert_before(self, target, data):
    if self.head == None:
      self.head = Node(data)
      return True
    else:
      node = self.tail
      while node.data != target:
        node = node.prev
        if node == None:
          return False
      new_node = Node(data)
      prev_node = node.prev
      prev_node.next = new_node
      new_node.prev = prev_node
      new_node.next = node
      node.prev = new_node
      return True
      
  def insert_after(self, target, data):
    if self.head == None:
      self.head = Node(data)
      return True
    else:
      node = self.head
      while node.data != target:
        node = node.next
        if node == None:
          return False
      new_node = Node(data)
      after_node = node.next
      after_node.preve = new_node
      new_node.next = after_node
      new_node.prev = node
      node.next = new_node
      return True
  
  def desc(self):
    node = self.head
    res = []
    while node:
      res.append(node.data)
      node = node.next
    print(res)

double_linked_list = NodeMgmt(0)
double_linked_list.desc() # [0]
for i in range(1, 10):
  double_linked_list.insert(i)
double_linked_list.desc() # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(double_linked_list.search_from_head(2))
print(double_linked_list.search_from_tail(8))
double_linked_list.search_from_tail(10) # Does Not Exist
double_linked_list.insert_before(2, 1.5)
double_linked_list.desc() # [0, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9]
double_linked_list.insert_after(5, 5.5)
double_linked_list.desc() # [0, 1, 1.5, 2, 3, 4, 5, 5.5, 6, 7, 8, 9]