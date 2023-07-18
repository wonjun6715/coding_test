def solution(nums):
    answer = 0
    s = list(set(nums))
    if len(s) > len(nums) // 2:
        return len(nums) // 2
    else:
        return len(s)