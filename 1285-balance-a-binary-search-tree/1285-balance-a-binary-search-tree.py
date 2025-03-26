# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        def sortedListToBST(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = sortedListToBST(nums[:mid])
            node.right = sortedListToBST(nums[mid+1:])
            return node
        
        sorted_values = inorder(root)
        
        return sortedListToBST(sorted_values)




