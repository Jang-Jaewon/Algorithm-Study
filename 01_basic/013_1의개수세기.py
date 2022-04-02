# 1부터 n까지 수 중 1의 갯수 구하기

# 풀이1
def solution(n):
    res = str(list(range(n+1))).count('1')
    return res
n = int(input())
print(solution(n))

# 풀이2
def solution(n):
    data = str(list(range(n+1)))
    count = 0
    for i in data:
        if i == '1':
            count += 1
    return count
n = int(input())
print(solution(n))