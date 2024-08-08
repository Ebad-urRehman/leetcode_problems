class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_dict = {}
        min_value = 0

        for char in text:
            if char in "balloon":
                if char not in char_dict:
                    char_dict[char] = 1
                else:
                    char_dict[char] += 1

        if all(char in char_dict for char in "balon"):
            char_dict['l'] //= 2
            char_dict['o'] //= 2
            min_value = min(char_dict.values())
        
        return min_value