class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        smap = {}
        pmap = {}
        
        for i in range(len(pattern)):
            if pattern[i] in smap:
                if smap[pattern[i]] != words[i]:
                    return False
            else:
                smap[pattern[i]] = words[i]
                
            if words[i] in pmap:
                if pmap[words[i]] != pattern[i]:
                    return False
            else:
                pmap[words[i]] = pattern[i]
        
        return True
