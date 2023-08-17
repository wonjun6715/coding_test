def solution(order):
    price = 0
    for i in range(len(order)):
        if 'latte' in order[i]:
            price += 5000
        else:
            price += 4500
    return price