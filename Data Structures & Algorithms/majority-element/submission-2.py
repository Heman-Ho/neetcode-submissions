class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Keep track of a tuple that represents a candidate for the maj element and it's frequency
        
        
        
        # After traversing the entire array, the candidate must be the maj element

        candidate = None
        freq = 0

        for num in nums:
            
            # add 1 to it's freq if the candidate appears in the array
            if num == candidate:
                freq += 1

            # If the candidate's freq is 0 and the current value != candidate, 
            # then switch the candidate to the current value and set it's frequency to 1.
            elif freq == 0:
                candidate = num
                freq = 1
            # if another elemnent is present, decrement the current candidate's frequency
            else:
                freq -= 1
            
        return candidate

