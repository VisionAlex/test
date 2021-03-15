def find_oldest_in_lineage(tree_data):
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

    # tree = {name : root[name] for name in names}
    # print(tree)
    return names


if __name__ == "__main__":
    tree_data = [
    ("Alex","Paul"),
    ("Alex","Marcela"),
    ("Dana","Paul"),
    ("Dana", "Marcela"),
    ("Paul", "Aneta"),
    ("Paul", " Mircea")
]
    ancestors = find_oldest_in_lineage(tree_data)
    print(ancestors)


