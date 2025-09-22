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

# Identify root nodes (nodes with no parent)
tree['type'] = 'Inner'
tree.loc[tree['p_id'].isnull(), 'type'] = 'Root'
# Identify leaf nodes (nodes that are not parents)
# NaNを除外してから判定
parent_ids = tree['p_id'].dropna()
leaf_nodes = tree[~tree['id'].isin(parent_ids)]
tree.loc[tree['id'].isin(leaf_nodes['id']), 'type'] = 'Leaf'
# Output id and type columns
tree = tree[['id', 'type']]
print(tree)