class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        newarr = []
        i  , j = 0 , 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                newarr.append(nums1[i])
                i+=1
            else:
                newarr.append(nums2[j])
                j+=1
        if i<len(nums1):
            newarr += nums1[i:]
        if j<len(nums2):
            newarr += nums2[j:]
        print(newarr)
        if len(newarr) % 2 != 0:
            mid = (len(newarr) + 0)//2
            print (newarr[mid])
            # return newarr[mid]
        else:
            m1 = ((len(newarr) + 0)//2)-1
            m2 = m1 + 1
            print(f"{newarr[m1]} ,{newarr[m2]}")
            # return ((newarr[m1] + newarr[m2])/2)

# Solution().findMedianSortedArrays([1,3],[2])
Solution().findMedianSortedArrays([1,2],[3,4])