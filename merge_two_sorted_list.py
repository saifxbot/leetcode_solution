class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # If one list is empty, return the other
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        tail = head  # tail points to the last node in the merged list

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return head
