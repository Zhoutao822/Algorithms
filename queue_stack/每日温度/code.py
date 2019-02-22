class Solution:
    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        """
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/218/stack-last-in-first-out-data-structure/879/
        递减栈，栈顶元素最小，栈底最大
        """
        ret = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop()
                ret[index] = i - index
            stack.append(i)
        return ret
        
t = [73,74,75,71,69,72,76,73]        
print(Solution().dailyTemperatures(t))