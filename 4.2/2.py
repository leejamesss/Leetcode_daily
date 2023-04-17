
# https://leetcode.cn/problems/integer-to-roman/
#哈希表
#打表列举
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        roman = ''
        for key in roman_dict:
            while num >= key:
                roman += roman_dict[key]
                num -= key
        return roman
