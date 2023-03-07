from fastapi import FastAPI, HTTPException
from typing import Optional, Dict, List
from pydantic import BaseModel
from fastapi.responses import RedirectResponse


# pydantic models for input data validation, not used in the algorithm itself
class Node(BaseModel):
    id: str
    left: Optional[str]
    right: Optional[str]
    value: int


class Tree(BaseModel):
    nodes: List[Node]
    root: str


class Model(BaseModel):
    tree: Tree


class BinaryTreeNode:
    def __init__(self, node_id: str, left, right, val: int):
        self.id = node_id
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val


def build_binary_tree(node_dict: Dict[str, BinaryTreeNode], root_id: str) -> Optional[BinaryTreeNode]:
    """
    Builds the binary tree iteratively from a dictionary of nodes starting from the root.
    """
    if not node_dict:
        return None

    def build_tree_helper(node_id: str) -> Optional[BinaryTreeNode]:
        if node_id is None:
            return None

        node = node_dict[node_id]
        left_child = build_tree_helper(node.left)
        right_child = build_tree_helper(node.right)

        return BinaryTreeNode(node.id, left_child, right_child, node.val)

    return build_tree_helper(root_id)


def max_path_sum(root: Optional[BinaryTreeNode]) -> int:
    """
    Time Complexity: O(N) since each node is visited only once where N is the number of nodes.
    Space Complexity: O(H) where H is the height of the tree and H= log(N) if the tree is balanced.
    in the worst case it is O(N) for a tree that is essentially a linked list.
    """
    if not root:
        return 0

    max_sum = root.val  # initial value to be overridden, also helps avoid edge case of tree with single node

    def max_path_sum_helper(node: BinaryTreeNode) -> int:
        nonlocal max_sum

        if node is None:
            return 0

        left_sum = max(max_path_sum_helper(node.left), 0)
        right_sum = max(max_path_sum_helper(node.right), 0)
        max_sum = max(max_sum, node.val + left_sum + right_sum)

        return node.val + max(left_sum, right_sum)

    max_path_sum_helper(root)

    return max_sum


app = FastAPI()


@app.get("/")
def redirect_to_docs():
    return RedirectResponse("/docs")


@app.post("/max-path-sum")
def get_max_path_sum(model: Model):
    # parse input tree
    tree = model.tree
    nodes = tree.nodes
    root_id = tree.root

    node_dict = {}
    for node in nodes:
        node_dict[node.id] = BinaryTreeNode(node.id, node.left, node.right, node.value)
    root = build_binary_tree(node_dict, root_id)
    return {"max_path_sum": max_path_sum(root)}  #
