def solution(numbers, direction):
    answer = []
    num1 = numbers[0]
    num2 = numbers[-1]
    if direction == 'right':
        numbers.remove(numbers[-1])
        numbers.insert(0, num2)
    else:
        numbers.remove(numbers[0])
        numbers.insert(len(numbers), num1)
    return numbers