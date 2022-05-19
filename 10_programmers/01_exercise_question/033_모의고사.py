# 모의고사
def solution(answers):
    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    res = []
    for i, answer in enumerate(answers):
      if answer == people1[i % len(people1)]:
        scores[0] += 1
      if answer == people2[i % len(people2)]:
        scores[1] += 1
      if answer == people3[i % len(people3)]:
        scores[2] += 1
    for i, score in enumerate(scores):
      if score == max(scores):
        res.append(i+1)
    return res

answers = [1,3,2,4,2]
print(solution(answers))