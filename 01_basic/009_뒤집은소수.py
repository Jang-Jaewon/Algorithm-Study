# 뒤집은 소수

# 풀이1
def is_prime():
  N = 100000
  check_list = [True] * (N+1)
  m = int(N ** 0.5)
  for i in range(2, m+1):
    if check_list[i] == True:
      for j in range(i+i, N+1, i):
        check_list[j] = False
  res = [i for i in range(2, N+1) if check_list[i] == True]
  return res
prime_list = is_prime()

def reverse(l):
  reverse_l = [int(str(i)[::-1]) for i in l]
  return reverse_l

l = [32, 55, 62, 3700, 250]
reverse_l = reverse(l)
for i in reverse_l:
  if i in  prime_list:
    print(i, end=' ')


# 풀이2
def reverse(x):
  res = 0
  while x > 0:
    t = x % 10
    res = res * 10 + t
    x = x // 10
  return res

def is_prime(x):
  if x == 0:
    return False
  for i in range(2, x//2+1):
    if x % i == 0:
      return False
  return True

n = 5
l = [32, 55, 62, 3700, 250]
for i in l:
  temp = reverse(i)
  if is_prime(temp):
    print(temp, end=' ')
