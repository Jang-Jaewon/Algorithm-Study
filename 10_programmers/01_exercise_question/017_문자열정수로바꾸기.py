# 문자열 정수로 바꾸기
def solution(s):
    if s[0] == "-":
      return int(s[1:]) * -1
    elif s[0] == "+":
      return int(s[1:])
    return int(s)
s = "-1234"
print(solution(s))