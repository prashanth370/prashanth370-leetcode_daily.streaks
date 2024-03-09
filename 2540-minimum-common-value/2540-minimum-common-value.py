class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        flag = -1
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                flag = nums1[i]
                break  # Once we find the common value, we can exit the loop
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        if flag == -1:
            return -1
        else:
            return flag
