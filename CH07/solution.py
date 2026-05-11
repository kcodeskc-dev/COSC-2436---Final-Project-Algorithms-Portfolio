# solution.py

from typing import Optional, List

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None 
        self.right = None
   #left and right are like pointers in c++, formally pythons calls these references 

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data: int) -> None:
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current: Node, new_node: Node) -> None:
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def inorder_traversal(self) -> List[int]:
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[Node], result: List[int]) -> None:
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
        """^
        Perform an inorder traversal of the binary tree and
        return a list of the elements in sorted order.
        """
        # TODO: Implement the inorder traversal
        # 1. Create an empty list to store the traversal result.
        # 2. Use a recursive helper function to visit nodes in inorder:
        #    a. Traverse the left subtree
        #    b. Visit the node (add its data to the result list)
        #    c. Traverse the right subtree
        # 3. Return the result list.
        

    def search(self, data: int) -> bool:
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node: Optional[Node], data: int) -> bool:
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
        """^
        Search for a data value in the binary tree.
        """
        # TODO: Implement the search function
        # 1. Start at the root and check if the current node's data matches the search data.
        # 2. If it matches, return True.
        # 3. If the search data is less than the current node, search the left subtree.
        # 4. If the search data is greater than the current node, search the right subtree.
        # 5. If the data is not found, return False.

if __name__ == "__main__":
    # Test data: a list of integers to create a binary tree
    test_data = [7, 3, 9, 1, 5, 8, 10]
    
    # Create a binary tree and insert test data
    tree = BinaryTree()
    for number in test_data:
        tree.insert(number)
    
    # Perform an inorder traversal and print the sorted elements
    sorted_elements = tree.inorder_traversal()
    print(sorted_elements)
    
    # Test searching for an element in the tree
    search_result = tree.search(5)
    print(search_result)
    
    search_result = tree.search(11)
    print(search_result)
