class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] +=1;
            else:
                d[i] = 1;
        g = d;
        d = {}
        for i in t:
            if i in d:
                d[i] +=1;
            else:
                d[i] = 1;
        
        if len(s) != len(t):
            return False
       
            
        for i in s:
            if i not in d or i not in g:
                return False
            elif d[i] != g[i]:
                return False
        return True