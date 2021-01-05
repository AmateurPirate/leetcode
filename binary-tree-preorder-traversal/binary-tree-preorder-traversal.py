# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def go(node):
            if not node:
                return
            ans.append(node.val)
​
            go(node.left)
            go(node.right)
            
        go(root)
        
        return ans
