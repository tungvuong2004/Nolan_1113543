"""
 * Name: Nolan
 * Student ID: 1113543
 * Date of Submission: 11/28/2024
 *
 * Program to calculate the diameter of a binary tree.
 * The diameter of a binary tree is the number of nodes on the longest path between any two nodes.
 * This path may or may not include the root.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def construct_tree(level_order_values):
    if not level_order_values or level_order_values[0] == -1:
        return None
    root = Node(level_order_values[0])
    queue = [root]
    index = 1
    while index < len(level_order_values):
        current_node = queue.pop(0)
        if level_order_values[index] != -1:
            current_node.left_child = Node(level_order_values[index])
            queue.append(current_node.left_child)
        index += 1
        if index < len(level_order_values) and level_order_values[index] != -1:
            current_node.right_child = Node(level_order_values[index])
            queue.append(current_node.right_child)
        index += 1
    return root

def calculate_tree_diameter(root):
    max_diameter = [0]  # A list is used to store the result so it can be updated inside the helper function

    def calculate_height(node):
        if not node:
            return 0
        left_subtree_height = calculate_height(node.left_child)
        right_subtree_height = calculate_height(node.right_child)
        # Update the maximum diameter found so far
        max_diameter[0] = max(max_diameter[0], left_subtree_height + right_subtree_height + 1)
        return 1 + max(left_subtree_height, right_subtree_height)

    calculate_height(root)  # Initiates the height calculation which updates max_diameter
    return max_diameter[0]

# Input handling
level_order_input = input("Provide the level-order traversal of the binary tree (comma-separated): ").strip()
# Strip brackets if present
if level_order_input.startswith("[") and level_order_input.endswith("]"):
    level_order_input = level_order_input[1:-1]
# Convert the cleaned input into a list of integers
level_order_values = list(map(int, level_order_input.split(",")))

# Build the binary tree and calculate the diameter
binary_tree_root = construct_tree(level_order_values)
print("The diameter of the binary tree is:", calculate_tree_diameter(binary_tree_root))
