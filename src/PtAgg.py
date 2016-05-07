import math

class PtAgg(object):
    # This is a class with x,y location and a counter (so we can aggregate the x,y locations for each cluster)
    # This class is designed to be immutable.
    def __init__(self, x = 0.0, y = 0.0, cnt = 0):
        self.x = x
        self.y = y
        self.cnt = cnt

    def __str__(self):
        if self.cnt != 0:
            return '{0},{1},{2}'.format(self.x, self.y, self.cnt)
        else:
            return '{0},{1}'.format(self.x, self.y)

    def __add__(self, other):
        return PtAgg(self.x + other.x, self.y + other.y, self.cnt + other.cnt)

    def DistSqr(self, pt):
        return (self.x - pt.x)*(self.x - pt.x) + (self.y - pt.y)*(self.y - pt.y)
    
    def Normalize(self):
        assert self.cnt > 0
        return PtAgg(self.x/self.cnt, self.y/self.cnt, 1)

