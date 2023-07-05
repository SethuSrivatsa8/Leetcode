from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Initialize variables
        zeroCount = 0       # Number of zero's in the current window
        longestWindow = 0   # Length of the longest subarray with at most one zero
        start = 0           # Left end of the window

        # Iterate through the input list using index 'i'
        for i in range(len(nums)):
            # Check if the current element at index 'i' is zero
            # If it is zero, increment 'zeroCount' by 1
            zeroCount += (nums[i] == 0)

            # While 'zeroCount' is greater than 1, which means there are more than one zeros in the current window:
            while zeroCount > 1:
                # Check if the element at the left end of the window (start) is zero
                # If it is zero, decrement 'zeroCount' by 1 as we are moving the window to the right
                zeroCount -= (nums[start] == 0)
                # Move the left end of the window one step to the right
                start += 1

            # Update the length of the longest subarray with at most one zero
            # The length is given by the difference between the current index 'i' and the left end of the window 'start'
            longestWindow = max(longestWindow, i - start)

        # Return the length of the longest subarray with at most one zero
        return longestWindow
