# N = int(input())
N = 3
check_list = [0] * (N+1)

def solution(v):   
  if v == N+1: 
    res = [i for i in range(1, N+1) if check_list[i] == 1]
    print(res)
  else:
    check_list[v] = 1
    solution(v+1)
    check_list[v] = 0
    solution(v+1)
    
print(solution(1))