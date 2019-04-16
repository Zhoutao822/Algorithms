#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (30.46%)
# Total Accepted:    4.7K
# Total Submissions: 14.5K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
# 
#
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_dict = set(wordList)
        if endWord not in word_dict:
            return 0

        begin_word_set = {beginWord}
        end_word_set = {endWord}
        all_chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        level = 1
        while len(begin_word_set) > 0:
            # 开始遍历新的一层
            level += 1
            temp_word_set = set()
            for word in begin_word_set:
                # 标记该层所有元素为已删除 避免同层节点之间相连
                # 这里需要判断是因为beginWord不在字典中
                if word != beginWord:
                    word_dict.remove(word)

            for word in begin_word_set:
                for i, char in enumerate(word):
                    for c in all_chars:
                        if c == char:
                            continue
                        temp_word = word[:i] + c + word[i + 1:]
                        if temp_word in word_dict:
                            if temp_word in end_word_set:
                                return level
                            temp_word_set.add(temp_word)

            # 让begin_word_set始终作为更小的那个集合 减少运算量
            if len(temp_word_set) < len(end_word_set):
                begin_word_set = temp_word_set
            else:
                begin_word_set = end_word_set
                end_word_set = temp_word_set

        return 0

beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
print(Solution().ladderLength(beginWord, endWord, wordList))
