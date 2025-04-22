# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        oddStart = head
        evenStart = evenHead = head.next
        while True:
            if evenHead is None:
                break
            if evenHead.next is None:
                break
            head.next = evenHead.next
            head = head.next

            evenHead.next = head.next
            evenHead = evenHead.next
        
        head.next = evenStart
        return oddStart
            
            
        # oddStart = head
        # evenStart = evenHead = ListNode(0)
        
        # while True:
        #     if head.next is None:
        #         evenHead.next = None
        #         break
        #     evenHead.next = head.next
        #     evenHead = evenHead.next

        #     if head.next.next is None:
        #         break

        #     head.next = head.next.next
        #     head = head.next

        # head.next = evenStart.next

        # return oddStart

            
            
            

