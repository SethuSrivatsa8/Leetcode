class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]  # Initialize the maximum product as the first element
        min_prod = nums[0]  # Initialize the minimum product as the first element
        result = max_prod  # Initialize the result as the first element

        for i in range(1, len(nums)):
            if nums[i] < 0:
                # If the current number is negative, swap the max and min products
                max_prod, min_prod = min_prod, max_prod

            # Update the maximum and minimum products for the current element
            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])

            # Update the result with the maximum product encountered so far
            result = max(result, max_prod)

        return result