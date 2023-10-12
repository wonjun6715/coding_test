def solution(nums):
    pocket = list(set(nums))
    pick = len(nums) // 2
    
    return min(len(pocket), pick)