#. 23. Merge k Sorted Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        print(len(lists));
        print((lists[0]));
        if len(lists) ==0:
            return None;
        return self.mergeLL(list,0,len(lists));
        
    def merge2Lists(self,list1, list2):
        
        # finList = (list2 if (list1==None))else ((list1 if list2 == None) else None)
        
        finList = None;
        if list1==None:
            return list2;
        if list2 == None:
            return list1;
        if(list1.val <= list2.val):
                   finList = list1;
                   finlist.next = merge2Lists(list1.next,list2);
        else:
                   finList = list2;
                   finlist.next = merge2Lists(list1,list2.next);
        return finList;
                   
    
    def mergeLL(self,list,l,h):
        mid = (l+h)/2;
        if(l==h):
            return list;
        lf = self.mergeLL(list,l,mid);
        rt = self.mergeLL(list,mid+1,h);
        return self.merge2Lists(lf,rt);
    
