# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tempHead = head
        tempHead2 = head

        if head == None or head.next == None:
            return False

        while tempHead != None:
            print("temphead: ", tempHead.val)
            print("temphead2: ", tempHead2.val)
            if tempHead.next != None:
                tempHead = tempHead.next.next
            else:
                return False
            tempHead2 = tempHead2.next
            if tempHead == tempHead2:
                return True

        
        return False
