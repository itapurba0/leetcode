import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        tib=0

        for node in lists:
            if node:
                heapq.heappush(heap,(node.val,tib,node))
                tib += 1
        
        dummy = ListNode(0)
        curr = dummy

        while heap:
            val,tb,smallest = heapq.heappop(heap)

            curr.next=smallest
            curr= curr.next

            if smallest.next:
                heapq.heappush(heap,(smallest.next.val,tib,smallest.next))
                tib += 1
        
        return dummy.next
