
from decimal import *

class Scale(object):
    """Class for representing scaling bases and converting
    between them.

    A scaling basis is a range if numeric values from 0
    to some number greater than 0. For example, a percentage
    is a scaled value between 0 and 100.
    a Scale is represented as a maximal value and a numeric 
    scalar type such as int, float, or decimal. Non-integral
    Scales can have an optional precision argument.
    """

    def __init__(self, top, form=int, **kw):
        self.top = top

        if form in [int, float, decimal]:
            self.form = form
        else:
            raise TypeError

        self.prec = 0
        self.zero_inclusive = True
        self.top_inclusive = True

        if kw is not None:
            keys = kw.keys()
            if (form != int) and ('prec' in keys):
                precision = kw['prec']
                if type(precision) is int:
                    self.prec = precision
                else:
                    self.prec = int(precision)
            if 'incl_zero' in keys:
                self.zero_inclusive = kw['incl_zero']
            if 'inclusive' in keys:
                self.top_inclusive = kw['inclusive']

    def on_scale(self, value):
        if type(value) != self.form:
            return False
        else:
            if self.zero_inclusive:
                if self.top_inclusive:
                    return 0 <= value <= self.top
                else:
                    return 0 <= value < self.top
            else:
                if self.top_inclusive:
                    return 0 < value <= self.top
                else:
                    return 0 < value < self.top            


    def scale(self, value, from):
        """Convert from a value from different scaling 
        factor to this one."""        
        if not from.on_scale(value):
            raise ValueError
        else:
            
