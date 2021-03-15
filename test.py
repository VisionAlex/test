def build_tree(tree_data):
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
    # print (tree)
    return tree


def find_parent(tree, name):
    
    if name in tree.keys():
        return name
    while type(tree) is dict:
        for parent, children in tree.items():
            tree = children    
            if name in tree:
                return parent

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
]
    tree = build_tree(tree_data)
    # print(f"Oldest in lineage is {oldest}")
    name = find_parent(tree, 'Paul')
    print(name)
