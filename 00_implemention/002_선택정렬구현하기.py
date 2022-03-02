# 선택 정렬
import random
def select_sort(l):
  for i in range(len(l)-1):
    lowest_idx = i
    for j in range(i+1, len(l)):
      if l[lowest_idx] > l[j]:
        lowest_idx = j
    l[i], l[lowest_idx] = l[lowest_idx], l[i]
  return l

data = random.sample(range(1,100), 10)
print(f"{data} => {select_sort(data)}")