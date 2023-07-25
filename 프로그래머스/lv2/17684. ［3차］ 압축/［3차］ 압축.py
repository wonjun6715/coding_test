def solution(msg):
    answer = []
    dictionary = {1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E", 6 : "F", 7 : "G",
                 8 : "H", 9 : "I", 10 : "J", 11 : "K", 12 : "L", 13 : "M",
                 14 : "N", 15 : "O", 16 : "P", 17 : "Q", 18 : "R", 19 : "S",
                 20 : "T", 21 : "U", 22 : "V", 23 : "W", 24 : "X", 25 : "Y",
                 26 : "Z"}
    reverse_dict = dict(map(reversed, dictionary.items()))
    position = 0
    key = 27
    while position < len(msg):
        result = ''
        for i in range(position, len(msg)):
            result += msg[i]
            position += 1
            if result not in reverse_dict:
                reverse_dict[result] = key
                key += 1
                answer.append(reverse_dict[result[:-1]])
                position = i
                break
            if i == len(msg) - 1:
                answer.append(reverse_dict[result])
    return answer