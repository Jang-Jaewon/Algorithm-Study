# 사이수의 합
def solution(a, b):
    if a < b:
      answer = [i for i in range(a, b+1)]
      return sum(answer)
    else:
      answer = [i for i in range(b, a+1)]
      return sum(answer)
    return [a]

a, b = 5, 3
print(solution(a, b))