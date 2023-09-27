class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sNums = sorted(nums)
        solution = []

        for i, num in enumerate(sNums):
            # if first triplet is positive, since nums is sorted a solution is no longer possible and we break
            if num > 0:
                break
            # as long as were not on the first iteration, check that the first triplet does not equal the previous one
            if i > 0 and num == sNums[i-1]:
                # if so continue to the next iteration
                continue
            # declare pointers
            l, r = i + 1, len(sNums) - 1
            # terminating condition
            while l < r:
                # compute sum
                cSum = num + sNums[l] + sNums[r]
                if cSum > 0:
                    r -= 1
                elif cSum < 0:
                    l += 1
                else:
                    # if sum == 0 then append to solution array and shift both pointers
                    solution.append([num, sNums[l], sNums[r]])
                    l += 1
                    r -= 1
                    # check that left pointer doesnt equal previous iteration and check terminating condition, if both are true, increment
                    while sNums[l] == sNums[l-1] and l < r:
                        l += 1
        return solution