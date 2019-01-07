#! /usr/python3 


class Point(object):
    def __init__(self, dimension=2, coordinates=[0, 0], **kw):
        self.dimension = dimension
        self.coordinates = coordinates
        self.extend()

        self.color = 'white'
        if 'color' in kw.keys():
            self.color = kw['color']



    def extend(self, new_dim=None):
        if new_dim is not None and new_dim > self.dimension:
            self.dimension = new_dim

        if length(self.coordinates) < self.dimension:
            for i in range(self.dimension):
                self.coordinates.append(0)


    def __add__(self, addend, color=None):
        """Return a new point which is the sum of
        the coordinates of two points. While this
        is not very meaningful in itself, it is used
        to support operations for things composed of
        points such as rays."""
        hue = self.color
        if color is not None:
            hue = color

        if self.dimension < addend.dimension:
            self.extend(addend.dimension)
        elif self.dimension > addend.dimension:
            addend.extend(self.dimension)
        
        coord = []
        for i in range(self.dimension):
            coord[i] = self.coordinates[i] + addend.coordinates[i]
        
        return Point(self.dimension, coord, color=hue)


