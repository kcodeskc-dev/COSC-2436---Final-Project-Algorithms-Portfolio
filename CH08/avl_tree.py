"""
Lab 08: Balanced Trees
Implement AVL tree from Chapter 8.

Chapter 8 covers:
- BST problems (unbalanced = O(n))
- AVL Trees (self-balancing)
- Splay Trees
- B-Trees
"""
from typing import Optional, Any, List


class AVLNode:
    """AVL tree node with height tracking."""
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1


class AVLTree:
    """Self-balancing AVL tree."""
    def __init__(self):
        self.root: Optional[AVLNode] = None
    
    def height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0
    
    def balance_factor(self, node: AVLNode) -> int:
        return self.height(node.left) - self.height(node.right)
        
    def rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    
    def rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    
    def insert(self, value: Any) -> None:
        """Insert value and rebalance."""
        self.root = self._insert(self.root, value)
    
    def _insert(self, node: Optional[AVLNode], value: Any) -> AVLNode:
        if not node:
            return AVLNode(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.balance_factor(node)

        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
    
    def inorder(self) -> List[Any]:
        """Return sorted values."""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node: Optional[AVLNode], result: List) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(5)
    tree.insert(4)
    tree.insert(15)
    print("Inorder traversal of the AVL tree:", tree.inorder())
