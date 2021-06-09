import cmath

from decimal import Decimal, Context


def is_perfect_square(square, *, complex=False):
    """
    Things I like about this:
    * cmath.sqrt is really neat!
    * float.is_integer() is descriptive
    * complex.real and complex.imag are well named
    * Decimal(<number>).sqrt(<context>) is handy
    Things that I don't like:
    * logic is branchy: we handle complex numbers iff complex=True
    * special case stuff for high precision floats of non-complex input only
      means that complex/real behaviour is different again...
    *
    """
    if complex:
        root = cmath.sqrt(square)
        return root.real.is_integer() and root.imag.is_integer()
    if square < 0:
        return False
    high_precision_context = Context(prec=len(str(square))*2)
    return 0 == Decimal(square).sqrt(high_precision_context) % 1

