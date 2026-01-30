"""
My python module for calculating the square root of a number
using the Newton's method.
"""

from numpy import sqrt
def sqrt2(x, debug=False):
    """
    Inputs:
    x: the number
    debug: a boolean, to print iteration values
    """    
    s=1.
    tol = 1.0E-14

    for k in range(100):
        s_old = s
        s = 0.5*(s + x/s)
        if debug:
            print(f"At the {k}-th iteration, the value of s is {s}")
        if abs(s-s_old) < tol:
            break
    return s

def test_main():
    from numpy import sqrt
    xvalues=[0., 2., 100, 1.e6]
    for x in xvalues:
        print(f"Testing with x={x}")
        s=sqrt2(x)
        s_numpy=sqrt(x)
        print(f"sqrt2 s = {s}, numpy s = {s_numpy}")
        assert abs(s-s_numpy) < 1e-14, "Your sqrt does not agree with numpy sqrt"

    
