import enum
from dataclasses import dataclass
from typing import Optional


@dataclass
class Card:
    name: str
    weight: int


class NodeTypes(enum.Enum):
    ARCANE_ENERGY = Card("arcane_energy", 1)
    CHARACTER = Card("character", 2)
    TOME = Card("tome", 6)
    CORE = Card("core", 10)
    GOLD = Card("gold", 15)


@dataclass
class Node:
    node_name: NodeTypes
    node_cost: int
    gold_value: int = None
    arcane_value: int = None
    node_down_left: Optional['Node'] = None
    node_down_right: Optional['Node'] = None


def create_node(node_name, node_cost, gold_value=None, arcane_value=None):
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


row1_nodes = [
    create_node(NodeTypes.ARCANE_ENERGY, 500, arcane_value=200),
    create_node(NodeTypes.CHARACTER, 200),
    create_node(NodeTypes.CHARACTER, 200),
    create_node(NodeTypes.GOLD, 400, gold_value=75),
]
row2_nodes = [
    create_node(NodeTypes.GOLD, 800, gold_value=150),
    create_node(NodeTypes.CHARACTER, 400),
    create_node(NodeTypes.TOME, 800),
]
row3_nodes = [
    create_node(NodeTypes.ARCANE_ENERGY, 2000, arcane_value=250),
    create_node(NodeTypes.CHARACTER, 500),
    create_node(NodeTypes.CHARACTER, 500),
    create_node(NodeTypes.ARCANE_ENERGY, 2000, arcane_value=250),
]
row4_nodes = [
    create_node(NodeTypes.CHARACTER, 800),
    create_node(NodeTypes.CHARACTER, 6000),
    create_node(NodeTypes.CHARACTER, 800),
]
row5_nodes = [
    create_node(NodeTypes.CORE, 20000),
    create_node(NodeTypes.TOME, 4400),
    create_node(NodeTypes.CHARACTER, 3500),
    create_node(NodeTypes.ARCANE_ENERGY, 6000, arcane_value=500),
]
row6_nodes = [
    create_node(NodeTypes.CHARACTER, 2000),
    create_node(NodeTypes.GOLD, 4000, gold_value=300),
    create_node(NodeTypes.ARCANE_ENERGY, 6000, arcane_value=700),
]
row7_nodes = [
    create_node(NodeTypes.CHARACTER, 11000),
    create_node(NodeTypes.ARCANE_ENERGY, 11000, arcane_value=1000),
    create_node(NodeTypes.CHARACTER, 11000),
    create_node(NodeTypes.TOME, 15000),
]
row8_nodes = [
    create_node(NodeTypes.CHARACTER, 20000),
    create_node(NodeTypes.GOLD, 11000, gold_value=450),
    create_node(NodeTypes.CHARACTER, 20000),
]

rows = [row1_nodes, row2_nodes, row3_nodes, row4_nodes, row5_nodes, row6_nodes, row7_nodes, row8_nodes]

for i in range(len(rows) - 1):
    create_link(rows[i], "down_right", rows[i + 1])
    create_link(rows[i], "down_left", rows[i + 1])

ROWS = rows
