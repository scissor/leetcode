#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Only when count is odd do the forwarding
    def middleNode_4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        count = 0
        while head:
            if count & 1:
                mid = mid.next
            count += 1
            head = head.next
        return mid
    
    # Totorise and Hare
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Use list, but not faster (55%)
    def middleNode_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        count = 0
        temp = head
        while temp:
            count += 1
            nodes.append(temp)
            temp = temp.next

        mid = int(count * 0.5)
        return nodes[mid]

    # Brute solution, but the fastest
    def middleNode_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math 
        
        nodes = []
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        mid = math.floor(count * 0.5) 

        temp = head
        for i in range(mid):
            temp = temp.next

        return temp
        
# @lc code=end

