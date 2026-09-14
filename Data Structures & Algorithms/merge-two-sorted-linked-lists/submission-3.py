# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        head = final
        head1 = list1
        head2 = list2

        while head1 != None or head2 != None:
            if head2 == None:
                final.next = head1
                final = final.next
                head1 = head1.next
            elif head1 == None:
                final.next = head2
                final = final.next
                head2 = head2.next
            
            elif head1.val < head2.val:
                final.next = head1
                final = final.next
                head1 = head1.next
            elif head1 == None or head2.val < head1.val:
                final.next = head2
                final = final.next
                head2 = head2.next
            elif head1.val == head2.val:
                final.next = head1
                final = final.next
                head1 = head1.next

        return head.next
            
        