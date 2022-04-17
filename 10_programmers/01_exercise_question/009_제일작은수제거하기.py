# 제일 작은 수 제거하기
def solution(arr):
    min_idx = arr.index(min(arr))
    del arr[min_idx]
    if len(arr):
      return arr
    return [-1]

arr = [4,3,2,1]	
print(solution(arr))