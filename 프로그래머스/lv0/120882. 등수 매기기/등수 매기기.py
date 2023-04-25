def solution(score):
    answer = []
    result =[]
    for i in score:
        answer.append(sum(i))
    print(answer)
    sorted_answer = sorted(answer, reverse = True)
    for i in answer:
        result.append(sorted_answer.index(i)+1)
    return result