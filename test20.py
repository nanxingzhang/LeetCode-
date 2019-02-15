#算法20：
#括号匹配

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic={')':'(',']':'[','}':'{'}
        stack=[]
        for c in s:
            if c in dic:
                a=stack.pop() if stack else ' '
                if a != dic[c]:
                    return False
            else:
                stack.append(c)
        return not stack