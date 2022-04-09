# 이상한 엘리베이터

def solution(n):
    res = 0
    while True:
        if n % 7 == 0:
            res += n // 7
            return res
        n -= 3
        res += 1
        if n < 0:
            return -1
# n = int(input())
n = 24          
print(solution(n)) # 4