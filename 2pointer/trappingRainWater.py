class Solution:
    def trap(self, height: List[int]) -> int:
      pass
          




    # 2 pointer solution
    # l = 0, r = l+1
    # while height[r] < height[l] trappedRain += height[l] - height[r]
    # shift right pointer until height[r] > height[l]
    # l = r, r = l+1
    # return trapped rainwater