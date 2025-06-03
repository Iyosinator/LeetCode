# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            stack = []
            curr = prev_group_end.next

            for _ in range(k):
                if not curr:
                    return dummy.next 
                stack.append(curr)
                curr = curr.next

            while stack:
                prev_group_end.next = stack.pop()
                prev_group_end = prev_group_end.next

            prev_group_end.next = curr
        
        