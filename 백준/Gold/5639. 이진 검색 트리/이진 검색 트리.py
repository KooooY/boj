import sys
sys.setrecursionlimit(10**5)
trees = sys.stdin.readlines()

preorder_tree = [int(tree.rstrip()) for tree in trees]
count = 0

def order_translation(root, end):
    if root > end or root >= len(preorder_tree) or end >= len(preorder_tree):
        return
    high = end + 1
    for i in range(root+1, end+1):
        if preorder_tree[i] > preorder_tree[root]:
            high = i
            break
    if high == end + 1:
        order_translation(root+1, end)
    else:
        order_translation(root + 1, high - 1)
        order_translation(high, end)
    print(preorder_tree[root])

order_translation(0, len(preorder_tree) - 1)
