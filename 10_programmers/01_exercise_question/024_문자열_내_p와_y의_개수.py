# 문자열 내 p와 y의 개수
def solution(s):
    answer = 0
    s = s.lower()
    for i in s:
        if i == 'p':
            answer += 1
        elif i == 'y':
            answer -= 1
    if answer:
        return "false"
    return 'true'

s = "pPoooyY"
print(solution(s))
