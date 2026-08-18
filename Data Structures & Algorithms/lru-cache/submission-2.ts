class LRUNode {
    constructor(
        public key: number,
        public val: number = 0,
        public prev: LRUNode = null,
        public next: LRUNode = null) {
        this.key = key;
        this.val = val;
        this.prev = prev;
        this.next = next;
    }
}
class LRUCache {
    /**
     * @param {number} capacity
     */
    private head: LRUNode;
    private tail: LRUNode;
    private checkMap: Map<number, LRUNode>;
    private capacity: number;
    constructor(capacity: number) {
        this.capacity = capacity;
        this.checkMap = new Map();
        this.tail = new LRUNode(0);
        this.head = new LRUNode(0, 0, null, this.tail);
        this.tail.prev = this.head;
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key: number): number {
        // return value of the node and update list
        if (this.checkMap.has(key)) {
            let node = this.checkMap.get(key);
            this.updateList(node);
            return node.val;
        }

        return -1;

    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key: number, value: number): void {
        // check existing
        // update map
        let node: LRUNode;
        if (this.checkMap.has(key)) {
            node = this.checkMap.get(key);
            node.val = value;
            this.updateList(node);
            return;
        } 
        node = new LRUNode(key, value);
        this.updateList(node, false);
        this.checkMap.set(key, node);
        while (this.checkMap.size > this.capacity) {
            let leastUsed = this.head.next;
            this.head.next = leastUsed.next;
            leastUsed.next.prev = this.head;
            this.checkMap.delete(leastUsed.key);
        }
    }

    updateList(node: LRUNode, existing: boolean = true): void {
        if (existing) {
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }

        let recentNode = this.tail.prev;
        recentNode.next = node;
        node.next = this.tail;
        node.prev = recentNode;
        this.tail.prev = node;
    }
}
