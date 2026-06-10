# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       output = []
       self.traverse(root, output)
       return output 
    

    def traverse(self, root: Optional[TreeNode], output: List[int]):
        if root:
            self.traverse(root.left, output)
            output.append(root.val)
            self.traverse(root.right, output)
    

        
        