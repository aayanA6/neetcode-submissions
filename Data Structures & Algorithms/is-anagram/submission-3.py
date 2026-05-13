class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i,0) +1  
        r = hashmap.items()

        hashmap = {}
        for i in t:
            hashmap[i] = hashmap.get(i,0) +1
        s = hashmap.items()

        print(r,s)

        return r == s
