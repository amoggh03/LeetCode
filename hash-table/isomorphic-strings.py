class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        smap = {}
        tmap = {}
        currents=t[0]
        currentt=t[0]
        for i in range(len(s)):
            currents=s[i]
            currentt=t[i]
            if currents in smap:
                if smap[currents] != currentt:
                    return False
            else:
                smap[currents] = currentt
            
            if currentt in tmap:
                if tmap[currentt] != currents:
                    return False
            else:
                tmap[currentt] = currents

        return True