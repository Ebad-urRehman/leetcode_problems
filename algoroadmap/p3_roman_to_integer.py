class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        rom_to_int_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        no_list = []

        for i, char in enumerate(s):
            if i+1 < len(s):
                if char == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                    no_list.append(-1)            
                elif char == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                    no_list.append(-10)
                elif char == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                    no_list.append(-100)
                else:
                    no_list.append(rom_to_int_dict[char])
            else:
                no_list.append(rom_to_int_dict[char])
        return sum(no_list)
