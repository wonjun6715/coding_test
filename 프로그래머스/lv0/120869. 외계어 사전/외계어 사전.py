def solution(spell, dic):
    answer = 0
    for word in dic:
        for i in range(len(spell)):
            if spell[i] in word:
                answer += 1
            else:
                break
        if answer == len(word) and answer == len(spell):
            return 1
        else:
            answer = 0 
    return 2