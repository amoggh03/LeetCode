class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize result and current pointers
        result_head = ListNode()
        current = result_head
        
        carry = 0  # Initialize carry to 0
        
        while l1 or l2 or carry:
            total = carry
            
            if l1:
                total += l1.val
                l1 = l1.next
                
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10  # Calculate digit for current position
            carry = total // 10  # Calculate carry for next position
            
            # Create new node for result list and move current pointer
            current.next = ListNode(num)
            current = current.next
        
        return result_head.next  # Return the result list excluding the initial dummy node
