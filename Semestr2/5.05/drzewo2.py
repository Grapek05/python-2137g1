# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.parent = None

    
# root = Node(10)
# root.left = Node(5)
# root.right = Node(20)
# root.left.left = Node(3)
# root.left.right = Node(7)

# print("Wartość korzenia:", root.value)
# print("Wartość lewego dziecka:", root.left.value)
# print("Wartość prawego dziecka:", root.right.value)

# BST

class NodeBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = NodeBST(new_value)
                self.left.parent = self
            else:
                self.left.insert(new_value)
        else:
            if self.right is None:
                self.right = NodeBST(new_value)
                self.right.parent = self
            else:
                self.right.insert(new_value)

def search(self, target):
    if target == self.value:
        return self
    elif target < self.value and self.left is not None:
        return self.left.search(target)
    elif target < self.value and self.right is not None:
        return self.right.search(target)
    return None
    

def find_min(self):
    current = self
    while current.left is not None:
        current = current.left
    return current

def find_max(self):
    current = self
    while current.right is not None:
        current = current.right
    return current    

def delete(self, value):
    if value < self.value:
        if self.left is not None:
            self.left = self.left.delete(value)
        elif value > self.value:
            if self.right is not None:
                self.right = self.right.delete(value)

        else:
            # Węzeł do usunięcia
            if self.left is None and self.right is None:
                return None # bez dzieci
            elif self.left is None:
                self.left.parent = self.parent
                return self.right
            elif self.right is None:
                self.right.parent = self.parent
                return self.left
            else:
                # Węzeł z dwoma dziećmi
                min_node = self.right.find_min()
                self.value = min_node.value
                self.value = self.right.delete(min_node.value)
        return self


# przyklad uzycia
root = NodeBST(10)
root.insert(5)
root.insert(20)
root.insert(3)
root.insert(7)


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)


# Przykład użycia
print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
def preorder(node):
    if node is not None:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')

def tree_depth(node):
    if node is None:
        return 0
    else:
        left_depth = tree_depth(node.left)
        right_depth = tree_depth(node.right)
        return max(left_depth, right_depth) + 1
    
print("\nTree Depth:", tree_depth(root))