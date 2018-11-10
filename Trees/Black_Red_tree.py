#Formally, a red-black tree is a binary search tree with nodes colored red and black in a way that satisfies the following properties:
#Root Property: The root is black.
#Red Property: The children of a red node (if any) are black.
#Depth Property: All nodes with zero or one children have the same black depth,
#defined as the number of black ancestors. (Recall that a node is its ownancestor).
from Trees import TreeMap

class RedBlackTreeMap(TreeMap):
    ”””Sorted map implementation using a red - black  tree.”””
    class _Node(TreeMap._Node):
        __slots__= '_red'
