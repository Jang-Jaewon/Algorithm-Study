import random

def merge_sort(l):
  res = list()
  if len(l) <= 1:
    return l
  mid = len(l) // 2
  left = merge_sort(l[:mid])
  right = merge_sort(l[mid:])
  while left and right:
    if left[0] < right[0]:
      res.append(left.pop(0))
    else:
      res.append(right.pop(0))
  while left:
    res.append(left.pop(0))
  while right:
    res.append(right.pop(0))
  return res

data = random.sample(range(100), 10)
print(f"{data} => {merge_sort(data)}")

