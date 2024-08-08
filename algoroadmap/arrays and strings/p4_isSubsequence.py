class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        """
        For this solution I follow that approach
        traverse the substring characters.
        if any substring character is found in traversal of string t
        then ignore the previous letters from this index because some elements that might come after may also 
        become before that index
        """
        new_str = ""

        for char_sub_str in s:
            if len(t) != 0 and char_sub_str in t:
                index = t.index(char_sub_str)
                new_str += char_sub_str
                t = t[index+1:len(t)]

        if new_str == s:
            return True
        else:
            return False