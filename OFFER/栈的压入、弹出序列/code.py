# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        # 输入两个整数序列，第一个序列表示栈的压入顺序，
        # 请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
        # 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
        # 但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

        # if not pushV: return True
        # if set(pushV) != set(popV):
        #     return False
        # stack = []
        # last_index = 0
        # while popV:
        #     first = popV.pop(0)
        #     first_index = pushV.index(first)
        #     stack.extend(pushV[last_index:first_index])
        #     for num in popV:
        #         if num in stack:
        #             if num != stack.pop():
        #                 return False
        #     last_index = first_index+1
        # return True

        # better 
        if not pushV: return True
        if set(pushV) != set(popV): return False
        stack = []
        pop_index = 0
        for i in range(len(pushV)):
            stack.append(pushV[i])
            while stack and stack[-1] == popV[pop_index]:
                stack.pop()
                pop_index += 1
        return len(stack) == 0

a = [1,2,3,4,5]
b = [4,5,3,2,1]
c = [4,3,5,1,2]

print(Solution().IsPopOrder(a, b))