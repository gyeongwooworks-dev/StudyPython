def solution(n):
    a = n % 7
    answer = n / 7
    if a == 0 :
        return int(answer)
    else :
        return int(answer) + 1