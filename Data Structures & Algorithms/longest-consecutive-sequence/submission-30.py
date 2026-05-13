class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        S = set(nums)
        longest = 0
        for n in S:
            if (n-1) not in S:
                length = 0
                while (n+length) in S:
                    length +=1
                longest = max(length,longest)
        return longest
            