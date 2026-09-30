"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def iter_list_node(l: ListNode | None):
    while l:
        yield l.val
        l = l.next


def traverse_list_node(l: ListNode | None) -> int:
    return sum(digit * 10**i for i, digit in enumerate(iter_list_node(l)))


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        if not l1 and not l2:
            return None

        n1 = traverse_list_node(l1)
        n2 = traverse_list_node(l2)

        tot = n1 + n2
        digits = [int(digit) for digit in str(tot)]
        digits.reverse()

        l3 = ListNode(digits[0])
        current_node = l3
        for digit in digits[1:]:
            current_node.next = ListNode(digit)
            current_node = current_node.next

        return l3
