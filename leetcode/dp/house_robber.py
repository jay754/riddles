"""



Recurrence Tree for nums = [2, 7, 9, 3, 1]

Starting from the first house (i = 0):

                             robFrom(0)
                          /               \
                Rob 2 + robFrom(2)      robFrom(1)
                       /         \            /           \
         Rob 9 + robFrom(4)   robFrom(3)    Rob 7 + robFrom(3)    robFrom(2)
                /       \           /      \           /         \            /          \
     Rob 1 + robFrom(6)  robFrom(5)  Rob 3 + robFrom(5)  robFrom(4)  Rob 3 + robFrom(4) robFrom(3)
           |                      |                  |                      |                   |                   
          0                      0                 0                      0                   0                


"""

def rob(nums):
    def robFrom(i):
        # Base case: no more houses to rob
        if i >= len(nums):
            return 0
        
        # Recursive case: decide to rob or skip the current house
        rob_current = nums[i] + robFrom(i + 2)  # Rob house `i`
        skip_current = robFrom(i + 1)           # Skip house `i`
        
        # Return the maximum of robbing or skipping the current house
        return max(rob_current, skip_current)
 
    # Start robbing from the first house (index 0)
    return robFrom(0)

# Example usage
nums = [2, 7, 9, 3, 1]
print("Max amount that can be robbed:", rob(nums))