# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None or head == None:
            return
        point = head
        point2 = head
        count = 0
        while point.next:
            if count % 2 != 0:
                point2 = point2.next
            point = point.next
            count+=1
        # print(point.val)
        # print(point2.val)

        point2 = point2.next
        prev = point2
        curr = point2.next
        prev.next = None
        while curr:
            far = curr.next
            curr.next = prev
            prev = curr
            curr = far
        # while prev:
        #     print(prev.val)
        #     prev = prev.next
        head1 = head
        final = ListNode()
        while prev:
            final.next = head1
            final = final.next
            head1 = head1.next
            final.next = prev
            final = final.next
            prev = prev.next
        print(head1.val)
        print(final.val)
        if head1:
            final.next = head1
            final = final.next
        final.next = None




