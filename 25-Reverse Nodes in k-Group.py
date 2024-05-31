# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        arr = []
        dummy = head
        dum2 = head
        while(head):
            for i in range(k):
                if(dummy != None):
                    arr.append(dummy.val)
                    dummy = dummy.next
                else:
                    return head
            for j in range(k):
                dum2.val = arr[k-(j+1)]
                dum2 = dum2.next
            arr = []
        return head
            