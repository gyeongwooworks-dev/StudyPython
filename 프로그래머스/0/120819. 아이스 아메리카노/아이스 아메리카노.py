def solution(money):
    answer = []
    a = money // 5500
    b = money - (a * 5500)
    answer.extend([a,b])
    return answer