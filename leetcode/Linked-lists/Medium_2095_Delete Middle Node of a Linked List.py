# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Single loop approach. Slow and fast pointer
        if head.next is None:
            return None
        
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head


        # Double loop approach
        # start = head
        # length = 0
        # while head:
        #     length += 1
        #     head = head.next
        
        # if length == 1:
        #     return None

        # length = length // 2

        # prev = None
        # head = start
        # while length > 0:
        #     prev = head
        #     head = head.next
        #     length -= 1
        
        # prev.next = head.next
        # return start

