class Node:
    def __init__(self):
        self.children = {}
        self.last = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = Node()
            curr = curr.children[s]
        curr.last = True
                

    def search(self, word: str) -> bool:
        curr = self.root
        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return curr.last

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for s in prefix:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return True

        