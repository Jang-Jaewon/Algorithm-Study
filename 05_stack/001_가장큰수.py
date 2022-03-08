# 가장 큰 수(스택)
def solution(nums, N):
  nums = [int(i) for i in str(nums)]
  stack = []
  for i in nums:
    while stack and N > 0 and stack[-1] < i:
      stack.pop()
      N -= 1
    stack.append(i)
  if N != 0:
    stack = stack[:-N]
  res = int(''.join(map(str, stack)))
  return res
  
# nums, N = map(int, input().split())
nums, N = 5276823, 3
print(solution(nums, N))