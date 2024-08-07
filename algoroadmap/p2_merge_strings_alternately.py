class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # finding the shortest length word
        length = len(word1) if len(word1) < len(word2) else len(word2)
        last_index = 0
        result_str = ""

        for i in range(length):
            result_str += word1[i]
            result_str += word2[i]
            last_index = i

        if len(word1) == len(word2):
            pass
        elif len(word1) > len(word2):
            # diff = len(word1) - len(word2) -1
            result_str += word1[last_index+1:len(word1)]
        else:
            diff = len(word2) - len(word1)
            result_str += word2[last_index+1:len(word2)]

        return result_str