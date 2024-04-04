class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = ListNode()  # Initialize merged list head
        merged_curr = merged_head  # Initialize merged list current pointer
        
        while list1 and list2:
            if list1.val <= list2.val:
                merged_curr.next = list1  # Append smaller node to merged list
                list1 = list1.next  # Move list1 pointer to next node
            else:
                merged_curr.next = list2  # Append smaller node to merged list
                list2 = list2.next  # Move list2 pointer to next node
            
            merged_curr = merged_curr.next  # Move merged list pointer to the newly appended node
        
        # Append remaining nodes from list1 or list2 to merged list
        merged_curr.next = list1 if list1 else list2
        
        return merged_head.next  # Return the merged list excluding the dummy head node
