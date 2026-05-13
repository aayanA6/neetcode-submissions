class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        h=1
        for i in range(len(nums)):
            for q in range(len(nums)):
                if q is not i:
                    h = h*nums[q]
            output.append(h)
            h = 1
        return output