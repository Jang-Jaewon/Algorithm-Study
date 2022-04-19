# 콜라스의 추축
def solution(num):
    answer = 0
    while num != 1:
      answer += 1
      if answer > 500:
        return -1
      if num % 2:
        num = (num * 3) + 1
      else:
        num = num / 2
    return answer

num = 16
print(solution(num))