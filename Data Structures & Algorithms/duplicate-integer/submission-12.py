class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if d.get(i) != None:
                return True
            else:
                d[i]= i
        return False
             