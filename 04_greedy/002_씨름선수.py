# 씨름선수(greedy)
# 풀이1
def solution(players, N):
  players = sorted(players, reverse=True)
  cnt = 1
  temp = players[0]
  for i in range(1, len(players)):
    if players[i][1] > temp[1]:
      cnt += 1
      temp = players[i]
  return cnt

# N = int(input())
# players = [list(map(int, input().split())) for _ in range(N)]
N = 5
players = [[172, 67], [183, 65], [180, 70], [170, 72], [181, 60]]
print(solution(players, N))


# 풀이2
def solution(players, N):
  players = sorted(players, reverse=True)
  largest = 0
  cnt = 0
  for height, weight in players:
    if max(weight, largest) == weight:
      cnt += 1
      largest = weight
  return cnt

# N = int(input())
# players = [list(map(int, input().split())) for _ in range(N)]
N = 5
players = [[172, 67], [183, 65], [180, 70], [170, 72], [181, 60]]
print(solution(players, N))