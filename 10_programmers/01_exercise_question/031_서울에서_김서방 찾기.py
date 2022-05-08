# 서울에서 김서방 찾기
def solution(seoul):
    res = seoul.index('Kim')
    return f"김서방은 {res}에 있다"


seoul = ["Jane", "Kim"]
print(solution(seoul))