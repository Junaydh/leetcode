class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      hash = {")": "(", "}" : "{", "]": "["}

      for char in s:
        if char not in hash:
          stack.append(char)
          continue
        if not stack or stack[-1] != hash[char]:
            return False
        stack.pop()
      
      return not stack
    # create hash with closing brackets as keys and corresponding opening brackets as values
    # loop through the string
    # while current char is not in our hash, add character to the stack
    # if it is in our hash, check that the last char added to our stack is it's corresponding opening bracket and pop
    # continue until stack is empty
    # return not stack because if stack is still populated after finishign the loop, our parentheses are not valid
