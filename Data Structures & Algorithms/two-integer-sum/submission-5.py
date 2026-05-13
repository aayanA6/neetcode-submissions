class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for q in range(len(nums)):
                if i != q and nums[q]+ nums[i] == target:
                    if i < q:
                        return [i,q]
                    else:
                        return [q,i]
               