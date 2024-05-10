class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left= left
        self.right = right
        

def isSameTree(self,p:TreeNode,q:TreeNode) ->bool:
    if not p and not q:
        return True
    if not q or not p:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)