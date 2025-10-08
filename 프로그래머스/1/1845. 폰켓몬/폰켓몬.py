def solution(nums):
    choice_set = set(nums)
    return min(len(choice_set), len(nums)/2)