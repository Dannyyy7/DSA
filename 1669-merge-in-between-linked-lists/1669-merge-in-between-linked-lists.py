# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        prev = list1
        for i in range(a - 1):
            prev = prev.next
        after = prev.next
        for i in range(b - a + 1):
            after = after.next
        prev.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = after
        return list1