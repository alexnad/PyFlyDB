from src.lib.utils import ensure_array


class Expression:
    '''
    A where (and other elements?) expression handler
    Contains a list of elements - variables, consts and operations
    '''

    def __init__(self, elements):
        self.elements = ensure_array(elements)

    # TODO probably not ...
    def validate_expression(self):
        pass


class SimpleGraphPatternExpression(Expression):
    def __init__(self, expr):
        """

        Args:
            expr (List[Node|Edge]):
        """
        Expression.__init__(self, expr)


class GraphPatternExpression(Expression):
    def __init__(self, simple_exprs):
        """

        Args:
            simple_exprs (SimpleGraphPatternExpression):
        """
        Expression.__init__(self, simple_exprs)


class OperatorExpression(Expression):
    def __init__(self, elements):
        Expression.__init__(self, elements)
