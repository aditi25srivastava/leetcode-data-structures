# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        inorder = [] # list for storing the inorder traversal
        curr = root 

        while curr:
            if curr.left is None: # Case 1: No left child
                inorder.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left # Case 2: Has a left child
                while prev.right and prev.right != curr:
                    prev = prev.right

                if prev.right is None:
                    prev.right = curr # Create temporary pointer 
                    curr = curr.left

                else:
                    prev.right = None
                    inorder.append(curr.val)
                    curr = curr.right

        return inorder                