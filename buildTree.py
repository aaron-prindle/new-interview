def buildTreeIndices(pLow,pHigh,inLow,inHigh,preorder, inorder):
  if inLow == inHigh:
    return None
  root = TreeNode(preOrder[pLow])
  rootPos = inorder.index(pLow)
  root.left = self.buildTreeIndices(1,1 + rootPos, 0, rootPos, preorder, inorder)
  root.right = self.buildTreeIndices(rootPos + 1, len(preorder), rootPos+1, len(inorder), preorder, inorder)
  return root

def buildTree(preorder, inorder):
  if not inorder: return None # inorder is empty
  root = TreeNode(preorder[0])
  rootPos = inorder.index(preorder[0])
  root.left = self.buildTreeIndices(1,1 + rootPos, 0, rootPos, preorder, inorder)
  root.right = self.buildTreeIndices(rootPos + 1, len(preorder), rootPos+1, len(inorder), preorder, inorder)
  return root
