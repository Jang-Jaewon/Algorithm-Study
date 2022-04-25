# 나누어 떨어지는 숫자배열
def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    if answer:
      return sorted(answer)
    return [-1]
arr = [2, 36, 1, 3]
divisor = 1
print(solution(arr, divisor))