#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Tortoise and hare (龜兔賽跑演算法)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
            
        return False
        
    
    # super slow
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        nodes = []
        
        while head:
            if head in nodes:
                return True
            
            nodes.append(head)
            head = head.next
        
        return False
        
# @lc code=end

