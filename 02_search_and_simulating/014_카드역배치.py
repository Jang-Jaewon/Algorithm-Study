# 카드 역배치
def solution(l):
  for _ in range(10):
    num1, num2 = map(int, input().split())
    cycle = (num2-num1+1)//2
    for i in range(cycle):
      l[num1+i], l[num2-i] = l[num2-i], l[num1+i]
  return l[1:]

l = list(range(21))
print(solution(l))