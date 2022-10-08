class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        i = list1
        j = list2
        k = z = ListNode()
        while (i and j):
            if i.val < j.val:
                k.next = i
                k = k.next
                i = i.next
            else:
                k.next = j
                k = k.next
                j = j.next
        if i == None:
            k.next = j
        else:
            k.next = i
        return z.next
            
# class Solution:
#     def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
#         while (list1 != None and list2 != None):
#             if list2 == None and list1 != None:
#                 return [list1.val]
#             if list1 == None and list2 != None:
#                 return [list2.val]
#             if list1 == None and list2 == None:
#                 return []
#             if list1.val >= list2.val:
#                 return [list2.val]+ self.mergeTwoLists(list1, list2.next)
#             else:
#                 return [list1.val]+ self.mergeTwoLists(list1.next, list2)