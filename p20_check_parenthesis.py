class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        for char in s:
            if char == '[' or char == '{' or char == '(':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == dict[char]:
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False