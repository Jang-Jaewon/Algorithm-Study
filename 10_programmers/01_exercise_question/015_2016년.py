# 2016년
def solution(a, b):
    answer = 0
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(a - 1):
        answer += months[i]
    answer += b
    answer = (answer % 7) - 3

    return days[answer]


a, b = 5, 24
print(solution(a, b))
