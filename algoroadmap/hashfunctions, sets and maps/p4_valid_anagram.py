class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach to Solution :
        Same approach as in previous problem
        pushing characters as key and their count as value in char_dict from s string

        deleting the characters as they encountered from t
        if all are deleted successfuly meaning s can be formed using different combination of  letters in t
        """
        char_dict = {}

        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

        for char in t:
            if char not in char_dict:
                return False
            elif char_dict[char] == 1:
                del char_dict[char]
            else:
                char_dict[char] -= 1
        
        if len(char_dict) == 0:
            return True
        else:
            return False