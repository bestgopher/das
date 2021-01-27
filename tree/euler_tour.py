class EulerTour:
    """
    Abstract base class for performing Euler tour of a tree.
    _hook_previsit and _hook_postvisit may be overridden by subclass.
    """

    def __init__(self, tree):
        """Prepare an Euler tour template for given tree."""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed."""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post visit of root."""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """
        Perform tour of subtree rooted at Position p.
        :param p: Position of current node being visited.
        :param d: depth of p in the tree.
        :param path: list of indices of children on path from root to p
        :return:
        """

        self._hook_previsit(p, d, path)
        result = []
        path.append(0)

        for c in self._tree.children():
            result.append(self._tour(c, d + 1, path))
            path[-1] += 1

        path.pop()
        return self._hook_postvisit(p, d, path, result)

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, result):
        pass


class PreorderPrintIndentedTour(EulerTour):

    def _hook_previsit(self, p, d, path):
        print(2 * d * " " + str(p.element()))


class PreorderPrintIndentedLabeledTour(EulerTour):

    def _hook_postvisit(self, p, d, path, result):
        label = ".".join(str(j + 1) for j in path)
        print(2 * d * " " + label, p.element())


class ParenthesizeTour(EulerTour):

    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:
            print(", ", end="")
        print(p.element(), end="")
        if not self.tree().is_leaf(p):
            print(" (", end="")

    def _hook_postvisit(self, p, d, path, result):
        if not self.tree().is_leaf(p):
            print(")", end="")


class DiskSpaceTour(EulerTour):

    def _hook_postvisit(self, p, d, path, result):
        return p.element().space() + sum(result)


class BinaryEulerTour(EulerTour):
    """
    Abstract base class for performing Euler tour of a binary tree.

    This version includes an additional _hook_invisit that is called after the tour
    of the left subtree(if any), yet before the tour of the right subtree(if any).

    Note: Right child is always assigned index 1 in path, even if no left sibling.
    """

    def _tour(self, p, d, path):
        result = [None, None]
        self._hook_previsit(p, d, path)

        if self._tree.left(p) is not None:
            path.append(0)
            result[0] = self._tour(self._tree.left(p), d + 1, path)
            path.pop()

        self._hook_invisit(p, d, path)

        if self._tree.right(p) is not None:
            path.append(1)
            result[1] = self._tour(self._tree.right(p), d + 1, path)

        return self._hook_postvisit(p, d, path, result)

    def _hook_invisit(self, p, d, path):
        pass


class BinaryLayout(BinaryEulerTour):
    """Class for computing (x, y) coordinates for each node of a binary tree."""

    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1
