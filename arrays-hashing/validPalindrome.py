import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s) <= 1):
            return True
        pattern = re.compile('[a-zA-Z0-9]')
        filtered, reverse = '', ''
        for char in s:
            if pattern.match(char):
                filtered += char
        filtered = filtered.lower()
        


    # remove all non letter chars
    # convert all to lowercase or uppercase
    # reverse string OR add first half to char array and then loop through check equality using negative indices
    # edge case: odd length of str - if str % 2 == 1: modify range