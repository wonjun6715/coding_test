def solution(numbers, target):
    idx = curr = 0
    def dfs(nums, target, curr, idx):
        if len(numbers) == idx:
            return 1 if curr == target else 0
        return dfs(nums, target, curr + nums[idx], idx + 1) \
               + dfs(nums, target, curr - nums[idx], idx + 1)
    answer = dfs(numbers, target, curr, idx)
    return answer
                     