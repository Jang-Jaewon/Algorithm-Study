# 문자열 속 문자 찾기

#풀이1
def func(data, target):
    i = 0
    if target not in data:
        return -1
    while True:
        if data[i:i+len(target)] == target:
            return i
        else:
            i += 1
data = input()
target = input()
print(func(data, target))

#풀이2
data = input()
target = input()
print(data.find(target))