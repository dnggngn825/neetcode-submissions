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
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head: ListNode | null): ListNode {
        if (!head) {
            return head;
        }

        let curr = head;
        let prev = null;
        while (curr.next) {
            let node = curr.next; // 2
            curr.next = prev // 1
            prev = curr
            curr = node
        }
        curr.next = prev

        return curr;
    }
}
