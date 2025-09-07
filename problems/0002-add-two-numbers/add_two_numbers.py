# ---------- Local testing version (use this in your repo) ----------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry, digit = divmod(total, 10)

            cur.next = ListNode(digit)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# ---------- Helpers for local pytest ----------
def list_to_linked(nums):
    """Convert Python list -> linked list."""
    dummy = ListNode()
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

def linked_to_list(node):
    """Convert linked list -> Python list."""
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out
