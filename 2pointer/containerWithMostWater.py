class Solution:
    def maxArea(self, height: List[int]) -> int:
        # declare pointers
        l,r= 0, len(height) -1
        # declare holder for solution and compute an initial area to compare against
        maxArea = min(height[l], height[r]) * (r-l)
        #terminating condition
        while l < r:
            #compute current area
            curArea = min(height[l], height[r]) * (r - l)
            # update maxArea if needed
            if curArea > maxArea:
                maxArea = curArea
            # shift the shorter pointer
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea