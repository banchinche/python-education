import pytest
from structures.tree import Tree


@pytest.mark.parametrize('given',
                         [
                             ([100, 200, 300, 400, 150, 120, 550, 880])
                         ])
def test_tree_init(given):
    tree = Tree()
    right = max(given)
    root = tree.insert(None, given[0])
    for i in range(1, len(given)):
        tree.insert(root, given[i])
    root_current = root
    while root_current is not None:
        root_current = root_current.right
        if root_current.right is None:
            break
    assert root_current.data == right


@pytest.mark.parametrize('given',
                         [
                             ([100, 200, 300, 400, 150, 120, 550, 880])
                         ])
def test_tree_traverse_inorder(capsys, given):
    tree = Tree()
    root = tree.insert(None, given[0])
    for i in range(1, len(given)):
        tree.insert(root, given[i])
    printed = ''
    for i in sorted(given):
        printed += f'{i}\n'
    tree.traverse_in_order(root)
    out, err = capsys.readouterr()
    assert out == printed
