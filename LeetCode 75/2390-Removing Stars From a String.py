class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:
            if i != '*':
                stack.append(i)
            else:
                if len(stack)>0:
                    stack.pop()
        a=""
        for i in stack:
            a=a+i
        return a