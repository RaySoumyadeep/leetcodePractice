'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 =[]
        n1 = l1
        n2 = l2
        while n1 is not None:
            list1.append(n1.val)
            n1 = n1.next
        while n2 is not None:
            list2.append(n2.val)
            n2 = n2.next
        list1 = list1[::-1]
        list2 = list2[::-1]
        ls = int(''.join(str(i) for i in list1)) + int(''.join(str(i) for i in list2))
        ls = [int(x) for x in str(ls)]
        ls = ls[::-1]
        out_ls = ListNode(ls[0])
        curr = out_ls
        for i in ls[1:]:
            temp = ListNode(i)
            curr.next = temp
            curr = temp
        return out_ls
        
