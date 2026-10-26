# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        #Get starting node
        if list1.val < list2.val:
            cur_node = list1
            list1 = list1.next 
        else:
            cur_node = list2
            list2 = list2.next
        
        merged_head = cur_node

        while list1 is not None and list2 is not None:

            if list1.val < list2.val:
                next_node = list1
                cur_node.next = list1
                list1 = list1.next

                cur_node = next_node
                
            else:
                next_node = list2
                cur_node.next = list2
                list2 = list2.next

                cur_node = next_node
        
        if list1 is not None:
            cur_node.next = list1
        else:
            cur_node.next = list2
    

        
        return merged_head
            



        






        


        