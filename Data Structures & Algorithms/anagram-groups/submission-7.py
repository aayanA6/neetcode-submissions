class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = {}
        for item in strs:
            hmap = {}
            for char in item:
                hmap[char] = hmap.get(char,0) +1
            curr = tuple(sorted(hmap.items()))
            if curr not in values:
                values[curr] = []
            values[curr].append(item)
        return list(values.values())

