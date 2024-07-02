import enum
from dataclasses import dataclass
from typing import Optional


@dataclass
class NameAndPriority:
    name: str
    weight: int


class NodeType(enum.Enum):
    ARCANE_ENERGY = NameAndPriority("arcane_energy", 1)
    CHARACTER = NameAndPriority("character", 2)
    TOME = NameAndPriority("tome", 6)
    CORE = NameAndPriority("core", 10)
    GOLD = NameAndPriority("gold", 15)


@dataclass
class Node:
    node_name: NodeType
    node_cost: int
    gold_value: int = 0
    arcane_value: int = 0
    node_down_left: Optional['Node'] = None
    node_down_right: Optional['Node'] = None


def create_node(node_name, node_cost, gold_value=0, arcane_value=0):
    return Node(node_name, node_cost, gold_value=gold_value, arcane_value=arcane_value)


def link_nodes(node1, direction, node2):
    if direction == "down_right":
        node1.node_down_right = node2
    elif direction == "down_left":
        node1.node_down_left = node2


def create_link(upper_row, direction, lower_row):
    length_of_row = len(upper_row) - 1

    if length_of_row == 3:
        if direction == "down_right":
            for i in range(length_of_row):
                link_nodes(upper_row[i], direction, lower_row[i])
        else:
            for i in range(length_of_row):
                link_nodes(upper_row[i + 1], direction, lower_row[i])
    else:
        if direction == "down_right":
            for i in range(length_of_row + 1):
                link_nodes(upper_row[i], direction, lower_row[i + 1])
        else:
            for i in range(length_of_row + 1):
                link_nodes(upper_row[i], direction, lower_row[i])


row0_nodes = [
    create_node(NodeType.ARCANE_ENERGY, 500, arcane_value=200),
    create_node(NodeType.CHARACTER, 200),
    create_node(NodeType.CHARACTER, 200),
    create_node(NodeType.GOLD, 400, gold_value=75),
]
row1_nodes = [
    create_node(NodeType.GOLD, 800, gold_value=150),
    create_node(NodeType.CHARACTER, 400),
    create_node(NodeType.TOME, 800),
]
row2_nodes = [
    create_node(NodeType.ARCANE_ENERGY, 2000, arcane_value=250),
    create_node(NodeType.CHARACTER, 500),
    create_node(NodeType.CHARACTER, 500),
    create_node(NodeType.ARCANE_ENERGY, 2000, arcane_value=250),
]
row3_nodes = [
    create_node(NodeType.CHARACTER, 800),
    create_node(NodeType.CHARACTER, 6000),
    create_node(NodeType.CHARACTER, 800),
]
row4_nodes = [
    create_node(NodeType.CORE, 20000),
    create_node(NodeType.TOME, 4400),
    create_node(NodeType.CHARACTER, 3500),
    create_node(NodeType.ARCANE_ENERGY, 6000, arcane_value=500),
]
row5_nodes = [
    create_node(NodeType.CHARACTER, 2000),
    create_node(NodeType.GOLD, 4000, gold_value=300),
    create_node(NodeType.ARCANE_ENERGY, 6000, arcane_value=700),
]
row6_nodes = [
    create_node(NodeType.CHARACTER, 11000),
    create_node(NodeType.ARCANE_ENERGY, 11000, arcane_value=1000),
    create_node(NodeType.CHARACTER, 11000),
    create_node(NodeType.TOME, 15000),
]
row7_nodes = [
    create_node(NodeType.CHARACTER, 20000),
    create_node(NodeType.GOLD, 11000, gold_value=450),
    create_node(NodeType.CHARACTER, 20000),
]

rows = [row0_nodes, row1_nodes, row2_nodes, row3_nodes, row4_nodes, row5_nodes, row6_nodes, row7_nodes]

for i in range(len(rows) - 1):
    create_link(rows[i], "down_right", rows[i + 1])
    create_link(rows[i], "down_left", rows[i + 1])

ALL_ROWS = rows
TOP_ROWS = row0_nodes
