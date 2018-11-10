class TreeMap(LinkedBinaryTree, MapBase):

    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.elemant()._key
        def value(self):
            return self.element()._value

        def _subtree_search(self, p, k):

            if k==p.key():
                return p
            elif k<p.key():
                if self.left(p) is not None:
                    return self._subtree_search(self.left(p), k)
            else:
                if self.right(p) is not None:
                    return self._subtree_search(self.right(p), k)
            return p

        def _subtree_first_position(self, p):
            #"""Return Position of first item in subtree rooted at p.”””
            walk=p
            while self.left(walk) is not None:
                walk = self.left(walk)
            return walk

        def _subtree_last_position(self, p):
            walk = p
            while self.right(walk) is not None:
                walk = self.right(walk)
            return walk

        def first(self):
            return self._subtree_first_position(self.root()) if len(self)>0 else None

        def last(self):
            return self._subtree_last_position(self.root()) if len(self)>0 else None

        def before(self, p):

            self._validate(p) # inherited from LinkedBinaryTree
            if self.left(p):
                return self._subtree_last_position(self.left(p))
            else:
                walk=p
                above=self.parent(walk)
                while above is not None and walk==self.left(above):
                    walk=above
                    above=self.parent(walk)
                return above


