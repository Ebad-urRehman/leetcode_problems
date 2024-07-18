class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        encountered_word = False
        count = 0

        for char in reversed(s):
            if char == " ":
                if encountered_word:
                    return count
            else:
                count += 1
                encountered_word = True

        return count
    

# more readable but less optimal than above
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # trailing spaces removed this make it more complex in above solution a var is used to check if spaces are trailing
        s = s.rstrip()
        count = 0

        for char in reversed(s):
            if char == " ":
                if count > 0:
                    return count
            else:
                count += 1 
        return count