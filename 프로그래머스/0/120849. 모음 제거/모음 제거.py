
def solution(my_string):
    alpha = ("a,e,i,o,u")
    answer =''
    for i in my_string[:]:
        if i not in alpha:
            answer += i
    return answer