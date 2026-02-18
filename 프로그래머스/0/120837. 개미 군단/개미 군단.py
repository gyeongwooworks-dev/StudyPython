def solution(hp):
    answer = 0
    a = hp % 5
    b = hp // 5
    c = a % 3
    d = a // 3
    answer = b + d + c
    return answer