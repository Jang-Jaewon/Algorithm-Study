# 없는 숫자 더하기
def solution(numbers):
    answer = [i for i in range(10) if i not in numbers]
    return sum(answer)

numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))