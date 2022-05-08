# 소수찾기
def solution(n):
    check_list = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if check_list[i] == True:
            for j in range(i + i, n + 1, i):
                check_list[j] = False
    res = [i for i in range(2, n + 1) if check_list[i] == True]
    return len(res)

n = 100
print(solution(n))