class Solution(object):
    def canThreePartsEqualSum(self, A):
        """ 将数组三等分
        :type A: List[int]
        :rtype: bool
        """
        target = sum(A) // 3
        if target * 3 != sum(A):
            return False
        i, j = 0, len(A) - 1
        sum1, sum2 = A[0], A[len(A) - 1]
        while i + 1 < j:
            if sum1 == target and sum2 == target:
                return True
            if sum1 != target:
                i += 1
                sum1 = sum1 + A[i]
            if sum2 != target:
                j -= 1
                sum2 += A[j]
        return False 

n = [3,3,6,5,-2,2,5,1,-9,4]
print(Solution().canThreePartsEqualSum(n))