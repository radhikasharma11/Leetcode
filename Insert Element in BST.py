# Insert element in BST
# There are no duplicates in BST. All nodes in BST are unique

class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# def insert(root, val):
#     if root is None or root.val == val:
#         return Node(val)
#     else:
#         if root.val > val:
#             return insert(root.left, val)
#         return insert(root.right, val)

class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

r = TreeNode(50)
s = Solution()
r = s.insertIntoBST(r, 30)
r = s.insertIntoBST(r, 20)
r = s.insertIntoBST(r, 40)
r = s.insertIntoBST(r, 70)
r = s.insertIntoBST(r, 60)
r = s.insertIntoBST(r, 80)

########################################3
# Another Solution
# class Solution:
#     def insertIntoBST(self, root, val):
#         def dfs(root):
#             if val < root.val:
#                 if root.left:
#                     dfs(root.left)
#                 else:
#                     root.left = TreeNode(val)
#             else:
#                 if root.right:
#                     dfs(root.right)
#                 else:
#                     root.right = TreeNode(val)
#
#         if not root: return TreeNode(val)
#         dfs(root)
#         return root