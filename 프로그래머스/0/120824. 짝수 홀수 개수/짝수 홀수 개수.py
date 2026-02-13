def solution(num_list):
    answer = [num%2 for num in num_list]
    return [answer.count(0), answer.count(1)]
        