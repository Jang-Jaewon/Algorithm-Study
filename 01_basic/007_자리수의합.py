# 자리수의 합
# 풀이1
def digit_sum(N, l):
  ll = [list(str(i)) for i in l]
  sum_l = [sum(map(int, i)) for i in ll]
  d = dict(zip(sum_l, l))
  return d[max(d)]
N = 3
l = [125, 15232, 97]
print(digit_sum(N, l)) # 97

# 풀이2
def digit_sum(digit):
  sum = 0
  while digit > 0:
    sum += digit % 10
    digit = digit // 10
  return sum

def solution(N, l):
  sum_l = [digit_sum(i) for i in l]
  d = dict(zip(sum_l, l))
  return d[max(d)]
N = 3
l = [125, 15232, 97]
print(solution(N, l)) # 97