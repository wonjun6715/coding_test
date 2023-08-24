def solution(polynomial):
    answer = ''
    polynomial = polynomial.replace(' ', '')
    polynomial = polynomial.split('+')
    tmp = ''
    a = []
    b = []
    for p in polynomial:
        print(p)
        if p[-1] == 'x':
            if p[0] == 'x':
                a.append(1)
            else:
                tmp = p[0:len(p) - 1]  
                a.append(int(tmp))
        else:
            b.append(int(p))
    if a and b:
        if sum(a) == 1:
            return 'x + {}'.format(sum(b))
        else:
            return '{}x + {}'.format(sum(a), sum(b))
    elif a:
        if not b:
            if sum(a) == 1:
                return 'x'
            else:
                return '{}x'.format(sum(a))
    elif b:
        if not a:
            return '{}'.format(sum(b))
                