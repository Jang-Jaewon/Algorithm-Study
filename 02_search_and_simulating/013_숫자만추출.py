# 숫자만 추출
# 풀이1
def solution(data):
  only_num = [i for i in data if 48 <= ord(i) <=57]
  num = int("".join(only_num))
  prime_list = [i for i in range(1, num+1) if num % i == 0]
  return num, len(prime_list)

# data = input()
data = "g0en2Ts8eSoft"
answer = solution(data)
for i in answer:
  print(i)

# 풀이2
def solution(data):
  num = 0
  cnt = 0 
  for i in data:
    if i.isdecimal():
      num = num * 10 + int(i)
  for i in range(1, num+1):
    if num % i == 0:
      cnt += 1
  return [num, cnt]

# data = input()
data = "g0en2Ts8eSoft"
answer = solution(data)
for i in answer:
  print(i)