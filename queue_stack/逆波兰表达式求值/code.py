class Solution:
    def evalRPN(self, tokens: 'List[str]') -> 'int':
        """
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/218/stack-last-in-first-out-data-structure/880/
        """
        stack = []
        op_list = ['+', '-', '*', '/']

        def cal(op, num1, num2):
            if op is '+': return num1 + num2
            if op is '-': return num1 - num2
            if op is '*': return num1 * num2
            if op is '/': return int(num1 / num2)

        for c in tokens:
            if c not in op_list:
                stack.append(int(c))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(cal(c, num1, num2))
        return stack[-1]

t = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(t))

