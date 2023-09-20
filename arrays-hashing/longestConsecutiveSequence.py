class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # construct set to remove non-unique nums
        setNums = set(nums)
        # create holder var for longest sequence
        longest = 0
        # iterate through set of nums
        for num in setNums:
            # check if current number is the beginning of the sequence
            if (num - 1 not in setNums):
                # declare length var
                length = 1
                # continue adding to length as long as the sequence keeps going
                while (num + length in setNums):
                    length += 1
                # after exiting while loop, we check if  that length is longer than the longest sequence so far
                longest = max(length, longest)
        # return longest
        return longest