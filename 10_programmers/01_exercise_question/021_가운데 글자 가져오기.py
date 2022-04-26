# 가운데 글자 가져오기
def solution(s):
    mid = len(s) // 2
    if len(s) % 2:
      return s[mid]
    return s[mid-1:mid+1]

s = "qwer"
print(solution(s))
