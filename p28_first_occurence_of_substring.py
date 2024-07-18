class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_length = len(needle)
        starting_letter = needle[0]

        for i, char in enumerate(haystack):
            if char == starting_letter and haystack[i:needle_length+i] == needle:
                return i
        
        return -1

