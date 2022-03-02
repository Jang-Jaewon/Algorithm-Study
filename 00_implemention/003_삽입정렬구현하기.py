# 삽입 정렬
import random
def insert_sort(l):
  for i in range(len(l)-1):
    for j in range(i+1, 0, -1):
      if l[j] < l[j-1]:
        l[j], l[j-1] = l[j-1], l[j]
      else: break
  return l

data = random.sample(range(1,100), 10)
print(f"{data} => {insert_sort(data)}")