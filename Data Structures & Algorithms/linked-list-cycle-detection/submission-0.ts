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
     * @return {boolean}
     */
    hasCycle(head: ListNode | null): boolean {
        let checkMap = new Map<ListNode, number>();
        let index = 0;
        let curr = head;
        while (curr) {
            if (checkMap.has(curr)) {
                return true;
            } else {
                checkMap.set(curr, index);
                curr = curr.next;
                index++;
            }
        }

        return false;
    }
}
