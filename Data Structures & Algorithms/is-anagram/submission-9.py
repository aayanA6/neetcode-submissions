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
        r = d
        
        if len(s) > len(t):
            l = s
        else:
            l = t
            
        for i in l:
            if i not in r or i not in g:
                return False
            elif r[i] != g[i]:
                return False
        return True