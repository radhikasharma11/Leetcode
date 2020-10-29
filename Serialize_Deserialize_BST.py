# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    #to print the tree
    def __str__(self):
        i = 0
        ret = "\t" * (i+1) + repr(self.val) + "\n"
        tr = [self.left, self.right]
        for child in tr:
            ret += child.__str__()
        return ret

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return "X"
        left_subtree = self.serialize(root.left)
        right_subtree = self.serialize(root.right)
        return str(root.val) + "," + left_subtree + "," + right_subtree

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """
        nodes = data.split(",")
        self.point = 0
        
        def deserialize_helper():
            if nodes[self.point] == "X":
                self.point += 1
                return None
            root = TreeNode(int(nodes[self.point]))
            self.point += 1
            root.left = deserialize_helper()
            root.right = deserialize_helper()
            return root

        return deserialize_helper()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(12)
# root.right.left = TreeNode(10)
# root.right.right = TreeNode(14)
str(root)
print(root)
tree = ser.serialize(root) # root = [2,1,3] Inorder
ans = deser.deserialize(tree)
str(ans)
print(ans)