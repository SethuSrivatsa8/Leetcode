class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_ending = nums[0]  # Initialize the maximum sum as the first element
        min_ending = nums[0]  # Initialize the minimum sum as the first element
        max_so_far = abs(nums[0])  # Initialize the maximum absolute sum encountered so far

        for i in range(1, len(nums)):
            max_ending = max(nums[i], max_ending + nums[i])
            min_ending = min(nums[i], min_ending + nums[i])
            max_so_far = max(max_so_far, abs(max_ending), abs(min_ending))

        return max_so_far
