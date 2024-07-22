from game_data import ALL_ROWS, TOP_ROW, NodeType

current = TOP_ROW[0]
flattened_graph = [col for row in ALL_ROWS for col in row]

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


def find_all_of_type(object_type):
    return [(object.row, object.col) for object in flattened_graph if object.node_name.name == object_type.name]

nodes_with_type = find_all_of_type(NodeType.GOLD)
print("here")
