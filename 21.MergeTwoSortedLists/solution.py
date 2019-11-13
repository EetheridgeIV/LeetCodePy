# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def insertList(head: ListNode, node: ListNode):
    node.next = None
    tempNode = head 
    while tempNode.next not None:
        tempNode = tempNode.next
    tempNode.next = node
    return
    
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        initVal = 0
        if(head1.val > head2.val):
            initVal = head2.val
        else:
            initVal = head1.val
        
        newHead = ListNode(initVal) 
        
        while head1.next not None and head2.next not None:
            if(head1.val > head2.val):
                insertlist(newHead, head2)
                head2 = head2.next
            else:
                insertList(newHead, head1):
                head1 = head1.next
        
        # Either list 1 is empty, list2 is empty or both are done
        if(head1.next == None and head2.next == None): # both on last node
            if(head1.val > head2.val):
                insertList(newHead, head2)
                insertList(newHead, head1)
                return newHead
        elif(head1.next == None):
            if(head1.val > head2.val):
                insertList(newHead, head2)
                insertList(newHead, head3)
                return newHead
        