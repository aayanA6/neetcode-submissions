class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i,0) +1  
        hashmap2 = {}
        for i in t:
            hashmap2[i] = hashmap2.get(i,0) +1

        return hashmap == hashmap2
