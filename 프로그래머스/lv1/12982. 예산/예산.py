def solution(d, budget):
    answer = 0
    price = 0
    d.sort()
    for i in range(len(d)):
        price += d[i]
        if price > budget:
            break
        answer += 1
    return answer
    
