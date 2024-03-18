class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        arrows = 1
        end = points[0][1]
        
        for balloon in points[1:]:
            if balloon[0] > end: 
                arrows += 1  
                end = balloon[1] 
            else:
                end = min(end, balloon[1])
        
        return arrows



























#         Intuition
# The problem asks for the minimum number of arrows needed to burst all balloons. Since the arrows can only be shot vertically, we need to find non-overlapping intervals of balloons and shoot arrows to cover each interval.

# Approach
# First, we sort the balloons based on their end coordinates. This allows us to iterate through the balloons in ascending order of their end coordinates.
# We initialize the variable arrows to 1, assuming that at least one arrow is needed.
# We iterate through the sorted balloons and compare the start coordinate of the current balloon with the end coordinate of the previous balloon.
# If the start coordinate of the current balloon is greater than the end coordinate of the previous balloon, it means these two balloons do not overlap, so we need to shoot another arrow. We increment the arrows count and update the prevEnd variable to the end coordinate of the current balloon.
# After iterating through all balloons, arrows will contain the minimum number of arrows needed.
# Complexity
# Time complexity: O(n*log(n))
# Space complexity: O(n)