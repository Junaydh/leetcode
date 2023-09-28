class Solution:
    def isValid(self, s: str) -> bool:
      pass


    # create hash with closing brackets as keys and corresponding opening brackets as values
    # loop through the string
    # while current char is not in our hash, add character to the stack
    # if it is in our hash, check that the last char added to our stack is it's corresponding opening bracket and pop
    # continue until stack is empty
    