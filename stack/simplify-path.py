class Solution:
    def simplifyPath(self, path: str) -> str:
        words=path.split('/')
        stack=[]
        for x in words:
            if x=="..":
                if stack:
                    stack.pop()
            elif x=="" or x==".":
                continue
            else:
                stack.append(x)  
        return "/"+"/".join(stack)                 
        
        