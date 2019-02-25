class Solution(object):
    def addBinary(self, a, b):
        """
        url: https://leetcode-cn.com/explore/learn/card/array-and-string/200/introduction-to-string/779/
        :type a: str
        :type b: str
        :rtype: str
        """
        def str2int(s):
            s = list(s)
            length = len(s)
            sum = 0
            for i in range(length):
                sum += int(s[i]) * 2 ** (length - i - 1)
            return sum
        sum = str2int(a) + str2int(b)
        return str(bin(sum))[2:]
        # return bin(int(a,2)+int(b,2))[2:]
a = "1010"
b = "1011"

print(Solution().addBinary(a, b))

