class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")":
                if not stack:
                    return False
                x = stack.pop()
                if x != "(":
                    return False
            elif i == "}":
                if not stack:
                    return False
                x = stack.pop()
                if x != "{":
                    return False
            elif i == "]":
                if not stack:
                    return False
                x = stack.pop()
                if x != "[":
                    return False
        return len(stack) == 0
