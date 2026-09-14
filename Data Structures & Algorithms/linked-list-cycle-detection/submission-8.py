# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        
        fast = head.next
        slow = head
        while fast and fast.next != None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        
        return False