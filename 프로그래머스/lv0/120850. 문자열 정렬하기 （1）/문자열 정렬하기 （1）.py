def solution(my_string):
    answer = []
    for nums in my_string:
        if nums.isalpha() == 0:
            answer.append(int(nums))
    answer.sort()
    return answer