# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res=[]
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def ok(root, depth):
            if not root:
                return None
            if depth==len(res):
                res.append(root.val)
            ok(root.right, depth+1)
            ok(root.left, depth+1)

            
        ok(root,0)
        return res
        