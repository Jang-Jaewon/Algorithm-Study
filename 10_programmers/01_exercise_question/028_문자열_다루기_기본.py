# 문자열 다루기 기본
def solution(s):
  return s.isdecimal() and len(s) in (4,6)

s = '1234'
print(solution(s))
