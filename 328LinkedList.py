__author__ = 'zhengyiwang'
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddhead = head
        if head is None or head.next is None or head.next.next is None:
            return head
        evenhead = oddhead.next
        oddcur = oddhead
        evencur = evenhead
        cur = head.next.next
        count = 3
        while cur is not None:
            if count % 2 == 1:
                oddcur.next = cur
                oddcur = cur
            else:
                evencur.next = cur
                evencur = cur
            cur = cur.next

            count+= 1
        oddcur.next = evenhead
        evencur.next = None
        return oddhead


if __name__ == "__main__":
    t = Solution()
    x = ListNode(1)
    y = ListNode(2)
    z = ListNode(3)
    x.next = y;
    y.next = z;
    t.oddEvenList(x)
