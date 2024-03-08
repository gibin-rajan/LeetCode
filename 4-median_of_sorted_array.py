class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        list=nums1+nums2
        list.sort()
        if len(list)%2!=0:

            C=len(list)//2
            
            return list[C]
        else:
            S=len(list)//2
            st=S-1
            p=(list[S]+list[st])/2.0
            return p