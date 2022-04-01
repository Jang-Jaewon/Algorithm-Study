res = []
def solution(n, start, end, mid):
    if n == 1:
        res.append([start, end])
        return None
    solution(n-1, start, mid, end)
    res.append([start, end])
    solution(n-1, end, mid, start)

# n = int(input())
n = 3
solution(n, 'A', 'C', 'B')
print(res, len(res))