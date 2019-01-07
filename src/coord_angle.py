#! python3

from math import *

class Theta(object):
    def __init__(self, coeff=0, expt=1):
        """An angle in a unspecified geometric dimension.
        Contains a value in radians represented as a coefficient 
        and an exponent, which are applied to pi.

        For example, an angle of 12/pi would be "Theta(12, -1)".
        """

        self.coeff = coeff
        self.expt = expt

