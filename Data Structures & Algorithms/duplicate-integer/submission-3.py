class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for q in range(len(nums)):
                if i != q and nums[q] == nums[i]:
                    return True 
        return False