class Solution:

    """
    Approach to Solution :
    pushing characters as key and their count as value in char_dict from magazine string

    deleting the characters as they encountered from ransomNote
    if all are deleted successfuly meaning substring(ransomnote) can be formed using letters in magazine(string)
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_dict = {}
        for char in magazine:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

        for char in ransomNote:
            if char not in char_dict:
                return False
            elif char_dict[char] == 1:
                del char_dict[char]
            else:
                char_dict[char] -= 1
            
        return True
    
# https://leetcode.com/problems/ransom-note/