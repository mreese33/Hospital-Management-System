
class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None


    def insert(self, parent_name, doctor_name, side):
        if self.root is None:
            print("The doctor tree is empty.")
            return

        parent = self.find_doctor(self.root, parent_name)

        if parent is None:
            print("Manager not found.")
            return

        side = side.lower()

        if side == "left":
            if parent.left is None:
                parent.left = DoctorNode(doctor_name)
                print(doctor_name, "added successfully.")
            else:
                print("The left position is already taken.")

        elif side == "right":
            if parent.right is None:
                parent.right = DoctorNode(doctor_name)
                print(doctor_name, "added successfully.")
            else:
                print("The right position is already taken.")

        else:
            print("Invalid side. Please enter left or right.")

    def find_doctor(self, node, name):
        if node is None:
            return None

        if node.name == name:
            return node

        left_result = self.find_doctor(node.left, name)

        if left_result is not None:
            return left_result

        return self.find_doctor(node.right, name)

    def preorder(self, node):
        if node is None:
            return []

        return ([node.name] +
                self.preorder(node.left) +
                self.preorder(node.right))

    def inorder(self, node):
        if node is None:
            return []

        return (self.inorder(node.left) +
                [node.name] +
                self.inorder(node.right))

    def postorder(self, node):
        if node is None:
            return []

        return (self.postorder(node.left) +
                self.postorder(node.right) +
                [node.name])


# Test the DoctorNode and DoctorTree classes

tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")


# Test the three traversal methods
print("\nPreorder Traversal:")
print(tree.preorder(tree.root))

print("\nInorder Traversal:")
print(tree.inorder(tree.root))

print("\nPostorder Traversal:")
print(tree.postorder(tree.root))


# Test edge cases
print("\nTesting Edge Cases:")

# Test a manager who does not exist
tree.insert("Dr. Smith", "Dr. Lee", "left")

# Test an invalid side
tree.insert("Dr. Croft", "Dr. Brown", "middle")

# Test a position that is already taken
tree.insert("Dr. Croft", "Dr. White", "left")

