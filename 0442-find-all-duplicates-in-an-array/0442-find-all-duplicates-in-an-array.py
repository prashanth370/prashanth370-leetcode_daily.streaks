class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        duplicates = []
        for i in nums:
            i = abs(i)
            if nums[i-1] <0:
                duplicates.append(i)
            nums[i-1] *= -1

        return duplicates
        # d = {}
        # for i in nums:
        #     if i in d:
        #         d[i] +=1
        #     else:
        #         d[i] = 1
            
        # return (zip(d.values(), d.keys()))






# Example input: nums = [4, 3, 2, 7, 8, 2, 3, 1]

# We initialize an empty list called ans to store the duplicates found in the input list.

# We determine the length of the input list nums and store it in the variable n. In this case, n = 8.

# We iterate through each element x in the nums list:

# For the first iteration, x = 4.

# We take the absolute value of x, which remains 4.
# We check if nums[4-1] is negative. Since nums[3] = 7 (not negative), we proceed.
# We mark nums[4-1] as visited by making it negative: nums[3] = -7.
# For the second iteration, x = 3.

# We take the absolute value of x, which remains 3.
# We check if nums[3-1] is negative. Since nums[2] = 2 (not negative), we proceed.
# We mark nums[3-1] as visited by making it negative: nums[2] = -2.
# For the third iteration, x = 2.

# We take the absolute value of x, which remains 2.
# We check if nums[2-1] is negative. Since nums[1] = 3 (not negative), we proceed.
# We mark nums[2-1] as visited by making it negative: nums[1] = -3.
# For the fourth iteration, x = 7.

# We take the absolute value of x, which remains 7.
# We check if nums[7-1] is negative. Since nums[6] = 3 (not negative), we proceed.
# We mark nums[7-1] as visited by making it negative: nums[6] = -3.
# For the fifth iteration, x = 8.

# We take the absolute value of x, which remains 8.
# We check if nums[8-1] is negative. Since nums[7] = 1 (not negative), we proceed.
# We mark nums[8-1] as visited by making it negative: nums[7] = -1.
# For the sixth iteration, x = 2.

# We take the absolute value of x, which remains 2.
# We check if nums[2-1] is negative. Since nums[1] = -3 (negative), we append 2 to the ans list.
# For the seventh iteration, x = 3.

# We take the absolute value of x, which remains 3.
# We check if nums[3-1] is negative. Since nums[2] = -2 (negative), we append 3 to the ans list.
# For the eighth iteration, x = 1.

# We take the absolute value of x, which remains 1.
# We check if nums[1-1] is negative. Since nums[0] = -4 (negative), we do nothing.
# Finally, we return the ans list, which contains [2, 3].

# So, the output derived from the given input is [2, 3].

# tc and sc = O(n) and O(1)