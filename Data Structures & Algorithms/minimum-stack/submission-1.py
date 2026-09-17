class Node:
    def __init__(self, val, prev, nxt):
        self.val = val
        self.prev = prev
        self.nxt = nxt
class MinStack:
    def __init__(self):
        self.stack = []
        self.minHead = Node(0, None, None)

    def push(self, val: int) -> None:
        temp = self.minHead
        while temp.nxt:
            if temp.nxt.val > val:
                node = Node(val, temp, temp.nxt)
                node.nxt.prev = node
                node.prev.nxt = node
                self.stack.append(node)
                print("push " + str(val))
                return
            else:
                temp = temp.nxt

        node = Node(val, temp, None)
        temp.nxt = node
        self.stack.append(Node(val, temp, None))
        print("push " + str(val))
            

    def pop(self) -> None:
        node = self.stack.pop()
        node.prev.nxt = node.nxt
        if (node.nxt):
            node.nxt.prev = node.prev
            

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.minHead.nxt.val
        
