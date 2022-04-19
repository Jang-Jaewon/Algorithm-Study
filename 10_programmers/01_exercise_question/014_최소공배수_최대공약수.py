# 최대공약수와 최소공배수
def gcd(n, m):
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd(n, m)
    return n


def solution(n, m):
    gcd_num = gcd(n, m)
    return [gcd_num, int(m * n / gcd_num)]


n, m = 2, 5
print(solution(n, m))
