from tree.linked_binary_tree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):

    def __init__(self, token, left=None, right=None):
        """
        Create an expression tree

        In a single parameter form, token should be a leaf value(e.g., '42'),
        and the expression tree will have that value at an isolated node.

        In a three-parameter version, token should be an operator,
        and left and right should be existing ExpressionTree instances that become
        the operands for the binary operator.
        """
        super().__init__()
        if not isinstance(token, str):
            raise TypeError("token must be a string")

        self._add_root(token)
        if left is not None:
            if token not in "+-*x/":
                raise ValueError("token must be valid operator")
            self._attach(self.root(), left, right)

    def __str__(self):
        """Return string representation of the expression."""
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return "".join(pieces)

    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append("(")
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)
            result.append(")")

    def evaluate(self):
        """Return the numeric result of the expression."""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_value = self._evaluate_recur(self.left(p))
            right_value = self._evaluate_recur(self.right(p))
            if op == "+":
                return left_value + right_value
            elif op == "-":
                return left_value - right_value
            elif op == "/":
                return left_value / right_value
            else:
                return left_value * right_value


def build_expression_tree(tokens):
    """Returns an ExpressionTree based upon by a tokenized expression."""
    s = []

    for t in tokens:
        if t in "+-*x/":
            s.append(t)
        elif t not in "()":
            s.append(ExpressionTree(t))
        elif t == ")":
            right = s.pop()
            op = s.pop()
            left = s.pop()

            s.append(ExpressionTree(op, left, right))

    return s.pop()
