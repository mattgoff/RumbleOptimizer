from game_data import ALL_ROWS, TOP_ROW, NodeType

current = TOP_ROW[0]


def search(current):
    while current:
        if current.node_name == NodeType.GOLD:
            print(f"{current.node_name.name=} {current.gold_value=}")
        else:
            print(f"{current.node_name.name=}")
        if current.node_down_left:
            search(current.node_down_left)
        if current.node_down_right:
            search(current.node_down_right)
        current = None


search(current)

print("here")
