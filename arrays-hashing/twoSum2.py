class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      l, r = 0, len(numbers) - 1

      while l < r:
        cSum = numbers[l] + numbers[l]
        if cSum == target:
          return [l+1, r+1]
        elif cSum < target:
          l += 1
        elif cSum > target:
          r -= 1