class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        result = prev = None
        while l1 and l2:
            data = l1.val + l2.val + carry
            carry, div = divmod(data, 10)
            if not result and not prev:
                result = prev = ListNode(val = div)
            else:
                prev.next = ListNode(val = div)
                prev = prev.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            data = l1.val + carry
            carry, div = divmod(data, 10)
            prev.next = ListNode(val = div)
            prev = prev.next
            l1 = l1.next
        while l2:
            data = l2.val + carry
            carry, div = divmod(data, 10)
            prev.next = ListNode(val = div)
            prev = prev.next
            l2 = l2.next
        if carry != 0:
            prev.next = ListNode(val = carry)
        
        return result
        