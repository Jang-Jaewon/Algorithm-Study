# 콤마찍기

# 풀이1
def solution(n):
    return format(n, ",")
n = 123456789
print(solution(n))


# 풀이2
def solution(n):
    if len(n) <= 3:
        return n
    else:
        return solution(n[:len(n)-3]) + ',' + n[len(n)-3:]
n = '123456789'
print(solution(n))