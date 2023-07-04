from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Create a defaultdict with Deg objects to store the start index,
        # end index, and count of each number in the array
        d = defaultdict(Deg)
        
        # Iterate over the array and update the start index, end index,
        # and count for each number
        for i, num in enumerate(nums):
            if num not in d:
                # If the number is encountered for the first time, update
                # its start index
                d[num].start = i
            # Update the end index and count for each occurrence of the number
            d[num].end = i
            d[num].count += 1
        
        # Find the maximum count (degree) among all numbers in the array
        max_count = max(d.values(), key=lambda x: x.count).count
        
        # Find the Deg objects with the maximum count
        degs_with_max_count = [x for x in d.values() if x.count == max_count]
        
        # Find the shortest subarray by calculating the length of each subarray
        # with the maximum count and taking the minimum length
        shortest_length = min(degs_with_max_count, key=lambda x: x.end - x.start)
        
        # Return the length of the shortest subarray
        return shortest_length.end - shortest_length.start + 1


# Define the Deg class to store the start index, end index, and count of a number
class Deg:
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0
