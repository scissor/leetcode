#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reverse = temp = None
        while slow:
            temp = slow.next
            slow.next = reverse
            reverse = slow
            slow = temp
            
        while reverse:
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next
        
        return True
   
    # Reverse half list with function
    def isPalindrome_3(self, head):
        def reverse(head):
            ans = next = None
            while head:
                next = head.next
                head.next = ans
                ans = head
                head = next
            return ans
        
        slow = fast = head 
        while fast != None and fast.next != None:
            slow = slow.next 
            fast = fast.next.next

        # Case for odd
        if fast != None: 
            slow = slow.next
        
        head2 = reverse(slow) 
        while head2 != None:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

    # Tortoise and hare
    def isPalindrome_2(self, head):
        reverse = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next

        if fast:
            slow = slow.next
            
        while reverse and reverse.val == slow.val:
            slow = slow.next
            reverse = reverse.next
        return not reverse


    # Brute solution with List, O(n) space
    def isPalindrome_1(self, head: Optional[ListNode]) -> bool:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        half_len = int(len(nums) / 2)
        for i in range(half_len):
            if nums[i] != nums[~i]:
                return False

        return True
        
# @lc code=end

