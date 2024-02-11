class TreeNode:
    def __init__(self, key):
        """
        Initialize a TreeNode with a key, left, and right child pointers.

        Parameters:
        - key: The value of the node.
        """
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        """
        Convert the TreeNode to a string.

        Returns:
        - str: String representation of the TreeNode.
        """
        return str(self.key)


class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty Binary Search Tree.
        """
        self.root = None

    def insert(self, key):
        """
        Insert a key into the Binary Search Tree.

        Parameters:
        - key: The value to be inserted into the tree.
        """
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        """
        Helper function to recursively insert a key into the Binary Search Tree.

        Parameters:
        - node: The current node being considered.
        - key: The value to be inserted into the tree.

        Returns:
        - TreeNode: The root of the modified tree.
        """
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        """
        Search for a key in the Binary Search Tree.

        Parameters:
        - key: The value to search for.

        Returns:
        - TreeNode or None: The node with the specified key, or None if not found.
        """
        return self._search(self.root, key)

    def _search(self, node, key):
        """
        Helper function to recursively search for a key in the Binary Search Tree.

        Parameters:
        - node: The current node being considered.
        - key: The value to search for.

        Returns:
        - TreeNode or None: The node with the specified key, or None if not found.
        """
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        """
        Delete a key from the Binary Search Tree.

        Parameters:
        - key: The value to be deleted.
        """
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """
        Helper function to recursively delete a key from the Binary Search Tree.

        Parameters:
        - node: The current node being considered.
        - key: The value to be deleted.

        Returns:
        - TreeNode or None: The root of the modified tree.
        """
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)
        return node

    def _min_value(self, node):
        """
        Helper function to find the minimum value in a subtree.

        Parameters:
        - node: The root of the subtree.

        Returns:
        - int: The minimum value in the subtree.
        """
        while node.left is not None:
            node = node.left
        return node.key

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the Binary Search Tree.

        Returns:
        - list: List of keys in ascending order.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        """
        Helper function to perform an inorder traversal of the Binary Search Tree.

        Parameters:
        - node: The current node being considered.
        - result: List to store the traversal result.
        """
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)


# Example usage:
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)
print("Inorder traversal:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
bst.delete(40)
print("Inorder traversal after deleting 40:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
