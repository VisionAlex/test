ddef build_tree(tree_data):
    #names with no parents
    names = set()
    root = {}
    for child, parent in tree_data:
        child_obj = root.get(child, None)
        if child_obj is None:
            child_obj = {}
            root[child] = child_obj
        else:
            names.discard(child)
        parent_obj = root.get(parent, None)
        if parent_obj is None:
            root[parent] = {child: child_obj}
            names.add(parent)
        else:
            parent_obj[child] = child_obj
    
    tree = {name : root[name] for name in names}
    return tree

def is_found(subtree,name):
    if type(subtree) is not dict:
        return False
    if name in subtree:
        return True
    for tree in subtree:
        is_found(tree, name)

def find_parent(tree, name):
    if name in tree:
        return name
    for item in tree:    
        if is_found(tree[item], name):
            return item
    


if __name__ == "__main__":
    tree_data = [
    ("Alex","Paul"),
    ("Alex","Marcela"),
    ("Dana","Paul"),
    ("Dana", "Marcela"),
    ("Paul", "Aneta"),
    ("Paul", "Mircea"),
    ('Aneta', 'Vasilica'),
    ('Aneta', 'Georgel'),
    ('MiniDana', 'Dana'),
]
    tree = build_tree(tree_data)
    print(tree)
    name = find_parent(tree, 'Dana')
    print(name)
