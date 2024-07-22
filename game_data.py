import enum
from dataclasses import dataclass
from typing import Optional


@dataclass
class NameAndPriority:
    name: str
    weight: int


class NodeType(enum.Enum):
    ARCANE_ENERGY = NameAndPriority("arcane_energy", 5)
    CHARACTER = NameAndPriority("character", 4)
    TOME = NameAndPriority("tome", 3)
    CORE = NameAndPriority("core", 1)
    GOLD = NameAndPriority("gold", 2)


@dataclass
class Node:
    node_name: NodeType
    node_cost: int
    row: int
    col: int
    gold_value: int = 0
    arcane_value: int = 0
    child_left: Optional['Node'] = None
    child_right: Optional['Node'] = None
    parent_left: Optional['Node'] = None
    parent_right: Optional['Node'] = None


def create_node(node_name, node_cost, row, col, gold_value=0, arcane_value=0):
    return Node(node_name, node_cost, row, col, gold_value=gold_value, arcane_value=arcane_value)


def link_nodes(node1, direction, node2):
    if direction == "child_right":
        node1.child_right = node2
    if direction == "child_left":
        node1.child_left = node2
    if direction == "parent_right":
        node1.parent_right = node2
    if direction == "parent_left":
        node1.parent_left = node2


def _link_nodes_according_to_collections(collection1, collection2, dir):
    for i in range(len(collection1)):
        link_nodes(collection1[i], dir, collection2[i])


def create_link(upper_row, direction, lower_row):
    if 'child' in direction:
        length_of_row = len(upper_row) - 1 if len(upper_row) == 4 else len(upper_row)
        start = 0 if direction == "child_right" else 1
        end = length_of_row if direction == "child_right" else length_of_row + 1
        _link_nodes_according_to_collections(upper_row[start:end], lower_row, direction)

    if 'parent' in direction:
        length_of_row = len(lower_row)
        start = 0 if direction == "parent_right" else 1
        end = length_of_row if len(lower_row) == 3 else length_of_row - 2
        _link_nodes_according_to_collections(lower_row[start:end], upper_row[start:end], direction)



row0_nodes = [
    create_node(NodeType.ARCANE_ENERGY, 500, 0, 0,arcane_value=200),
    create_node(NodeType.CHARACTER, 200,0 , 1),
    create_node(NodeType.CHARACTER, 200, 0, 2),
    create_node(NodeType.GOLD, 400, 0, 3, gold_value=75),
]
row1_nodes = [
    create_node(NodeType.GOLD, 800, 1, 0, gold_value=150),
    create_node(NodeType.CHARACTER, 400, 1, 1),
    create_node(NodeType.TOME, 800, 1, 2),
]
row2_nodes = [
    create_node(NodeType.ARCANE_ENERGY, 2000, 2, 0, arcane_value=250),
    create_node(NodeType.CHARACTER, 500, 2, 1),
    create_node(NodeType.CHARACTER, 500, 2, 2),
    create_node(NodeType.ARCANE_ENERGY, 2000, 2, 3, arcane_value=250),
]
row3_nodes = [
    create_node(NodeType.CHARACTER, 800,3, 0),
    create_node(NodeType.CHARACTER, 6000, 3, 1),
    create_node(NodeType.CHARACTER, 800, 3, 2),
]
row4_nodes = [
    create_node(NodeType.CORE, 20000, 4, 0),
    create_node(NodeType.TOME, 4400, 4, 1),
    create_node(NodeType.CHARACTER, 3500, 4, 2),
    create_node(NodeType.ARCANE_ENERGY, 6000, 4, 3, arcane_value=500),
]
row5_nodes = [
    create_node(NodeType.CHARACTER, 2000, 5, 0),
    create_node(NodeType.GOLD, 4000, 5, 1, gold_value=300),
    create_node(NodeType.ARCANE_ENERGY, 6000, 5, 2, arcane_value=700),
]
row6_nodes = [
    create_node(NodeType.CHARACTER, 11000, 6, 0),
    create_node(NodeType.ARCANE_ENERGY, 11000, 6, 1, arcane_value=1000),
    create_node(NodeType.CHARACTER, 11000, 6, 2),
    create_node(NodeType.TOME, 15000, 6, 3),
]
row7_nodes = [
    create_node(NodeType.CHARACTER, 20000, 7, 0),
    create_node(NodeType.GOLD, 11000, 7, 1, gold_value=450),
    create_node(NodeType.CHARACTER, 20000,7 ,2),
]

rows = [row0_nodes, row1_nodes, row2_nodes, row3_nodes, row4_nodes, row5_nodes, row6_nodes, row7_nodes]

# create child relationships
for i in range(len(rows) - 1):
    create_link(rows[i], "child_right", rows[i + 1])
    create_link(rows[i], "child_left", rows[i + 1])

# create parent relationships
for i in range(1, len(rows)):
    create_link(rows[i - 1], "parent_right", rows[i])
    create_link(rows[i - 1], "parent_left", rows[i])


ALL_ROWS = rows
TOP_ROW = row0_nodes
