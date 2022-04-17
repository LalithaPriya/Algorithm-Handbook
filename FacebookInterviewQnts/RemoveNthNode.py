#19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head;
        # curr = head;
        tot=0;
        while(head):
            tot+=1;
            head= head.next;
        head =temp;
        i=0;
        while(i<(tot-n)):
            i+=1;
            # if((tot-n)==i):
            #     cr = temp.next;
            # prev = temp;
            print(temp)
            temp = temp.next;
        if temp:
            temp.next = temp.next.next;
        
        print(tot);
        # print(curr)
        return temp
