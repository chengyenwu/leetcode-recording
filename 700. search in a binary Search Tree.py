# 700. Search in a binary Search Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        else: 
            if val == root.val:
                return root
            elif val < root.val:
                return self.searchBST(root.left, val)
            else:
                return self.searchBST(root.right, val)