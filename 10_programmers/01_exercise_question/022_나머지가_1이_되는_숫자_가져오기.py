# 나머지가 1이 되는 숫자 가져오기
def solution(n):
    answer = [i for i in range(1, n) if n % i == 1]
    return min(answer)
n = 12
print(solution(n))