# 행렬의 덧셈
def solution(arr1, arr2):
    outer_len = len(arr1)
    inner_len = len(arr1[0])
    for i in range(outer_len):
        for j in range(inner_len):
            arr1[i][j] += arr2[i][j]
    return arr1