# 최소값구하기
# 풀이1
def solution(arr, arrMin):
  for i in arr:
    if i < arrMin:
      arrMin = i
  return arrMin

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin=float('inf') # 👈 python에서 가장 큰 수(무한대)
print(solution(arr, arrMin))

# 풀이2
def solution(arr, arrMin):
  for i in range(1, len(arr)):
    if arr[i] < arrMin:
      arrMin = arr[i]
  return arrMin

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin=arr[0]
print(solution(arr, arrMin))
