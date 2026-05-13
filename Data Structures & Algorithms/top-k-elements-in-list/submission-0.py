class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        values = []
        for i in range(len(nums)):
            hmap[nums[i]] = hmap.get(nums[i],0) +1
        
    
        sorted_map = dict(sorted(hmap.items(), key=lambda x: x[1], reverse=True))
        sorted_map = list(sorted_map)
        for i in range(k):
            values.append(sorted_map[i])
        return values