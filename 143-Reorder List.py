class Solution:
  def reorderList(self, head):
    def findMid(head):
      prev = None
      slow = head
      fast = head

      while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
      prev.next = None

      return slow

    def reverse(head):
      prev = None
      curr = head

      while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

      return prev

    def merge(l1, l2):
      while l2:
        next = l1.next
        l1.next = l2
        l1 = l2
        l2 = next

    if not head or not head.next:
      return

    mid = findMid(head)
    reversed = reverse(mid)
    merge(head, reversed)