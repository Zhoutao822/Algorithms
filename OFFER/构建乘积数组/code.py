# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        # 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
        # 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
        left, right = [1], [1]
        _A = A[::-1]
        for i in range(len(A)-1):
            left.append(A[i] * left[-1])
            right.append(_A[i] * right[-1])
        return [x * y for x, y in zip(left, right[::-1])]

