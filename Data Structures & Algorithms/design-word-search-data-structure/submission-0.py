class Node:
    def __init__(self):
        self.children = {}
        self.last = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = Node()
            curr = curr.children[s]
        curr.last = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(node, i ,n):
            #condition to stop
            if i == n:
                return node.last
            
            if word[i] == ".":
                for no in node.children.values():
                    if dfs(no, i+1, n):
                        return True

            if word[i] in node.children:
                if dfs(node.children[word[i]], i+1, n):
                    return True
            
            return False

        return dfs(curr, 0, len(word))


