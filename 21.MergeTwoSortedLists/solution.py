# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head: ListNode):
    tempNode = head
    while(tempNode):
        if not tempNode.next:
            print(tempNode.val)
        else:
            print(tempNode.val, "-> ", end='')
        tempNode = tempNode.next

def insertList(head: ListNode, val):
    newNode = ListNode(val)
    tempNode = head
    while tempNode.next:
        tempNode = tempNode.next
    tempNode.next = newNode
    return

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    head1 = l1
    head2 = l2

    initVal = 0
    if(head1.val > head2.val):
        initVal = head2.val
        head2 = head2.next
    else:
        initVal = head1.val
        head1 = head1.next

    newHead = ListNode(initVal)

    while head1 and head2:
        if(head1.val > head2.val):
            insertList(newHead, head2.val)
            head2 = head2.next
        else:
            insertList(newHead, head1.val)
            head1 = head1.next
    # Either list 1 is empty, list2 is empty or both are done
    if(not head1 and not head2): # Both empty
        return newHead
    elif(not head1): # First list is empty
        while(head2):
            insertList(newHead, head2.val)
            head2 = head2.next
        return newHead
    elif(not head2): # Second list is empty
        while(head1):
            insertList(newHead, head1.val)
            head1 = head1.next
        return newHead

def main():
    head1 = ListNode(1)
    insertList(head1, 2)
    insertList(head1, 4)

    head2 = ListNode(1)
    insertList(head2, 3)
    insertList(head2, 4)

    newHead = mergeTwoLists(head1, head2)

    printList(newHead)
main()
