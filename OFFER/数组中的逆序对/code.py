# -*- coding:utf-8 -*-
# class Solution:
#     def InversePairs(self, data):
#         # write code here
#         # 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
#         # 输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 
#         # 即输出P%1000000007
#         # 题目保证输入的数组中没有的相同的数字

#         # 数据范围：

#         # 	对于%50的数据,size<=10^4

#         # 	对于%75的数据,size<=10^5

#         # 	对于%100的数据,size<=2*10^5
#         return self.helper(data[:], data[:], 0, len(data)-1) % 1000000007

    # def helper(self, tmp, data, start, end):
    #     if end - start < 1:
    #         return 0
    #     if end - start == 1:
    #         if data[start] <= data[end]:
    #             return 0
    #         else:
    #             tmp[start], tmp[end] = data[end], data[start]
    #             return 1
    #     mid = (start + end) // 2
    #     cnt = self.helper(tmp, data, start, mid) + self.helper(tmp, data, mid+1, end)
    #     print(mid, start, end)
        # i = mid
        # j = end
        # copy = end
        # while i >= start and j >= mid + 1:
        #     if data[i] > data[j]:
        #         tmp[copy] = data[i]
        #         cnt += j - mid
        #         i -= 1
        #     else:
        #         tmp[copy] = data[j]
        #         j -= 1
        #     copy -= 1
        # while i >= start:
        #     tmp[copy] = data[i]
        #     i -= 1
        #     copy -= 1
        # while j >= mid + 1:
        #     tmp[copy] = data[j]
        #     j -= 1
        #     copy -= 1
        # return cnt

# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        return self.inverseCount(data[:], 0, len(data)-1, data[:])%1000000007
       
    def inverseCount(self, tmp, start, end, data):
        if end-start <1:
            return 0
        if end - start == 1:
            if data[start]<=data[end]:
                return 0
            else:
                tmp[start], tmp[end] = data[end], data[start]
                return 1
        mid = (start+end)//2
        cnt = self.inverseCount(data, start, mid, tmp) + self.inverseCount(data, mid+1, end, tmp)
        # print(start, mid, end, cnt, data)
        i = start
        j = mid + 1
        ind = start
           
        while(i <= mid and j <= end):
            if data[i] <= data[j]:
                tmp[ind] = data[i]
                i += 1
            else:
                tmp[ind] = data[j]
                cnt += mid - i + 1
                j += 1
            ind += 1
        while(i<=mid):
            tmp[ind] = data[i]
            i += 1
            ind += 1
        while(j<=end):
            tmp[ind] = data[j]
            j += 1
            ind += 1
        return cnt
n = [1,2,3,4,5,6,7,0]
print(Solution().InversePairs(n))