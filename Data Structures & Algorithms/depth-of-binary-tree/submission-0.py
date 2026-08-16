# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, count):
            if not node:
                return count
            else:
                count+=1

            leftCount = dfs(node.left, count)
            rightCount = dfs(node.right, count)

            return max(leftCount, rightCount)
        return dfs(root, 0)