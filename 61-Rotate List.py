# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        # base case
        if not head or k == 0:
            return head

        # length of the linked list
        current = head
        length = 0
        while current:
            length+=1
            current = current.next

        # special k
        if k == length:
            return head
        k =  k % length
        if k == 0:
            return head
        
        # the number of times to move forward
        go = length - k
        first = head
        for i in range(go-1):
            first = first.next
        nextFirst = first.next
        first.next = None
        if length == 1:
            return head
        
        # connect two parts
        tail = nextFirst
        while tail.next:
            tail = tail.next
        tail.next = head
        return nextFirst