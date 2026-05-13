class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_two = []
        for i in nums:
            if i not in nums_two:
                nums_two.append(i)
            else:
                return True
        return False