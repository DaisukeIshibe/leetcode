import pandas as pd
'''
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
Each node in the tree can be one of three types:

"Leaf": if the node is a leaf node.
"Root": if the node is the root of the tree.
"Inner": If the node is neither a leaf node nor a root node.
Write a solution to report the type of each node in the tree.
'''
tree = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'p_id': [None, 1, 1, 2, 2]
})

def report_node_types(tree: pd.DataFrame) -> pd.DataFrame:
    node_types = []

    for _, row in tree.iterrows():
        node_id = row['id']
        parent_id = row['p_id']
        
        # Check if the node is a root
        if pd.isna(parent_id):
            node_type = 'Root'
        else:
            # Check if the node is a leaf
            if node_id not in tree['p_id'].values:
                node_type = 'Leaf'
            else:
                node_type = 'Inner'
        
        node_types.append({'id': node_id, 'type': node_type})
    
    return pd.DataFrame(node_types)