# 하샤드수
def solution(x):
    answer = True
    x_sum = sum([int(i) for i in str(x)])
    if x % x_sum:
      answer = False
    return answer

x = 10
print(solution(x))