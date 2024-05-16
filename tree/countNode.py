def countNode(self,root:TreeNode) ->int:
    if not root:
        return 0
    else :
        self.countNode(root.right)+self.countNodes(root.left)