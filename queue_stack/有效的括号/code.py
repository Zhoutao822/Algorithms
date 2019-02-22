class Solution:
    def isValid(self, s: 'str') -> 'bool':
        """
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/218/stack-last-in-first-out-data-structure/878/
        如果是左括号则入栈，如果是右括号则出栈，判断出栈括号是否与右括号相匹配，否则返回false，直到栈空
        """
        left = ['[', '{', '(']
        right = [']', '}', ')']
        stack = []
        for c in list(s):
            if c in left:
                stack.append(c)
            if c in right:
                if not stack or right.index(c) != left.index(stack.pop()):
                    return False
        if not stack:
            return True
        else:
            return False

s = ""
so = Solution()
print(so.isValid(s))
