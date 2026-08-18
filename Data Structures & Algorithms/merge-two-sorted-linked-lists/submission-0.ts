/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode {
        let curr1 = list1;
        let curr2 = list2;
        if (!curr1 && !curr2) return null;
        if (!curr1 || !curr2) return curr1 || curr2;
        let head = new ListNode();
        let result = head;
        while (curr1 && curr2) {
            let val1= curr1.val;
            let val2 = curr2.val;

            if (val1 < val2) {
                result.next = new ListNode(val1);
                curr1 = curr1.next;
            } else {
                result.next = new ListNode(val2);
                curr2 = curr2.next;
            }
            result = result.next;
        }

        result.next = curr1 || curr2;

        return head.next;

    }
}
