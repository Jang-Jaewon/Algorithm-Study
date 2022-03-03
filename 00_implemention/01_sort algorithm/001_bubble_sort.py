# 버블 정렬
import random
def bubble_sort(l):
  for i in range(len(l)-1):
    swap = False
    for j in range(len(l)-1-i):
      if l[j] > l[j+1]:
        l[j], l[j+1] = l[j+1], l[j]
        swap = True
    if swap == False: break
  return l

data = random.sample(range(1,100), 10)
print(f"{data} => {bubble_sort(data)}")