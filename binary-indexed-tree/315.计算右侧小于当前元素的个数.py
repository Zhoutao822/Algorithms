#
# @lc app=leetcode.cn id=315 lang=python
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (38.52%)
# Total Accepted:    2.1K
# Total Submissions: 5.6K
# Testcase Example:  '[5,2,6,1]'
#
# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
# 
# 示例:
# 
# 输入: [5,2,6,1]
# 输出: [2,1,1,0] 
# 解释:
# 5 的右侧有 2 个更小的元素 (2 和 1).
# 2 的右侧仅有 1 个更小的元素 (1).
# 6 的右侧有 1 个更小的元素 (1).
# 1 的右侧有 0 个更小的元素.
# 
# 
#
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or not len(nums):
            return []
        tmp=[]
        res=[]
        for i in reversed(nums):
            pos=self.bisert(tmp,i)
            res.append(pos)
        return list(reversed(res))
    
    def bisert(self,tmp,t):
        start=0
        end=len(tmp)-1
        while end>=start:
            mid=(start+end)>>1
            if tmp[mid]>t:
                end=mid-1
            else:
                start=mid+1
        index=start-1
        while index>=0 and tmp[index]==t:
                index-=1
        tmp.insert(index+1,t)
        return index+1
                
n = [5,2,6,1]
print(Solution().countSmaller(n))
