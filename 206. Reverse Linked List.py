# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Previous Node starts as None
        prev=None
        #current node starts from head
        curr=head
        while curr:
            next_node=curr.next
            curr.next=prev
            #Move prev forward
            prev=curr
            #Move curr forward
            curr=next_node
        return prev
