class Solution:
    def hasPathSum(self, root, targetSum):
        """
         :type root:TreeNode
         : type targetSum: int
        """
        if root == None:
            return False

        if (root.left == None and root.right == None and root.val == targetSum):
            return True

        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)



