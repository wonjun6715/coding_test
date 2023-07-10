def solution(s):
    k = []
    answer = ''
    alpha = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    
    for word in s:
        answer += word
        if answer in alpha:
            k.append(answer)
            answer = ''
        if answer in numbers:
            k.append(answer)
            answer = ''
    for i in range(len(k)):
        for j in range(len(alpha)):
            if k[i] == alpha[j]:
                k[i] = numbers[j]
    a = int(''.join(k))
    return a