# question 1

class Empty(Exception):
    pass

def subtree_min_and_max(subtree_root):
    min = subtree_root.data
    max = subtree_root.data

    if subtree_root.left != None:
        if (subtree_min_and_max(subtree_root.left))[0] < min:
            min = (subtree_min_and_max(subtree_root.left))[0]

        if (subtree_min_and_max(subtree_root.left))[1] > max:
            max = (subtree_min_and_max(subtree_root.left))[1]

    if subtree_root.right != None:
        if (subtree_min_and_max(subtree_root.right))[0] < min:
            min = (subtree_min_and_max(subtree_root.right))[0]

        if (subtree_min_and_max(subtree_root.right))[1] > max:
            max = (subtree_min_and_max(subtree_root.right))[1]

    return(min,max)


def min_and_max(bin_tree):
    if bin_tree.is_empty():
        raise Empty('Empty')

    min, max1 = subtree_min_and_max(bin_tree.root)

    return (min, max1)