class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, water = 0, len(height) - 1, 0
        lMax, rMax = height[l], height[r]

        # check if height array is empty
        if not height:
            return 0
        # terminating condition
        while l < r:
            # choosing smaller pointer to increment, if equal either works
            # in both blocks, we're adding the difference between the shorter boundary(lmax, rmax) and the current height, to our water variable
            # since we're taking the max of both of these values(lmax, current height) we're adding either a positive integer or 0
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                water += lMax - height[l]
            # same logic as above but when rmax < lmax OR if they are equal
            else:
                r -= 1
                rMax = max(rMax, height[r])
                water += rMax - height[r]
        return water
          




    # 2 pointer solution
    # l = 0, r = len(height)-1
    # we can disregard the first and last indexes because they dont have valid container boundaries
    # we only need to check the corresponding boundary for our pointer because as long as the opposite boundary is > or == to it, the local opposite boundary doesn't really matter
