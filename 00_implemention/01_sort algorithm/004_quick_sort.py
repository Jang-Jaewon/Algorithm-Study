import random

def quick_sort(l):
  if len(l) <= 1: 
    return l
  pivot = l[0]
  left = [i for i in l[1:] if pivot > i]
  right = [i for i in l[1:] if pivot <= i]
  return quick_sort(left) + [pivot] + quick_sort(right)

data = random.sample(range(100), 10)
print(f"{data} => {quick_sort(data)}")