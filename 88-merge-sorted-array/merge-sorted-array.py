class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m-1
        right = n - 1
        arr = len(nums1) - 1
        while left >= 0 and right >= 0:
            if nums1[left] < nums2[right]:
                nums1[arr] = nums2[right]
                right -= 1
            else:
                nums1[arr] = nums1[left]
                left -= 1
            arr -= 1
        while right >= 0:
            nums1[arr] = nums2[right]
            right -= 1
            arr -= 1


        
        # array1 = m-1
        # array2 = n-1
        # array = len(nums1)-1
        # while array1 >= 0 and array2 >= 0:
        #     if nums1[array1] > nums2[array2]:
        #         nums1[array] = nums1[array1]
        #         array1 -= 1
        #     else:
        #         nums1[array] = nums2[array2]
        #         array2 -= 1
        #     array -= 1
        # while array2 >= 0:
        #     nums1[array] = nums2[array2]
        #     array2 -= 1
        #     array -= 1
        
        