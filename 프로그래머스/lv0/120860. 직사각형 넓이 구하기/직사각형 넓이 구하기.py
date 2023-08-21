def solution(dots):
    x_set = []
    y_set = []
    for i in range(4):
        x_set.append(dots[i][0])
        y_set.append(dots[i][1])
    x_set_2 = sorted(list(set(x_set)))
    y_set_2 = sorted(list(set(y_set)))
    
    return (x_set_2[1] - x_set_2[0]) * (y_set_2[1] - y_set_2[0])