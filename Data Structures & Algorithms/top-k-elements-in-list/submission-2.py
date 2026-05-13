class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i,0) +1

        hmap = sorted(hmap.items(), key=lambda x: x[1], reverse=True)

        List= []
        for i in range(k):
            List.append(hmap[i][0])
        return List
        
        