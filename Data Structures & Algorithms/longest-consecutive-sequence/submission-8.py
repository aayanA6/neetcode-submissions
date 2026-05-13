class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k = 1
        j = 1
        current = [0]
        for i in nums:
            while i+j in nums:
                k +=1
                j+=1
                
            else:
                current.append(k)
                k = 1
                j = 1
        return max(current)
            
