# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        # 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
        # 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
        if not sequence: return False
        return self.helper(sequence, 0, len(sequence)-1)
    def helper(self, s, l, r):
        if l >= r: return True
        i = r
        while i > l and s[i-1] > s[r]: i -= 1
        for j in range(i-1, l-1, -1):
            if s[j] > s[r]: return False
        return self.helper(s, l, i-1) and self.helper(s, i, r-1)



n = [1,2,4,3,6,8,7,5]
print(Solution().VerifySquenceOfBST(n))
