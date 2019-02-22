class Solution:
    def decodeString(self, s: 'str') -> 'str':
        """
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/220/conclusion/890/
        """
        s = list(s)
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                str_list = str()
                while stack[-1] != '[':
                    str_list = stack.pop() + str_list 
                stack.pop()
                num_list = str()
                while stack and stack[-1].isdigit():
                    num_list = stack.pop() + num_list
                k = int(num_list)
                stack.append(k * str_list)
        return ''.join(stack)

s = "3[a2[bc]]"

print(Solution().decodeString(s))


