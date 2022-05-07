#validate-binary-search-tree
def isBST(self, head):
    if (head == None):
        return True
    if (head.left != None and head.left.val > head.val)or (head.right != None and head.right.val < head.val):
        return False
    if (!isBST(head.left) or !isBST(head.right)):
        return False
     
    return True
