class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head
        
        # Obtener la longitud de la lista enlazada
        length = 0
        itr = head
        while itr:
            length += 1
            itr = itr.next
        
        # Obtener la cantidad de pasos necesarios para rotar
        k = k % length
        
        # Si k es igual a 0, no es necesario rotar
        if k == 0:
            return head
        
        # Obtener el nodo en la posición (length - k)
        itr = head
        for i in range(length - k - 1):
            itr = itr.next
        
        # Hacer la rotación
        new_head = itr.next
        itr.next = None
        itr = new_head
        while itr.next:
            itr = itr.next
        itr.next = head
        
        return new_head