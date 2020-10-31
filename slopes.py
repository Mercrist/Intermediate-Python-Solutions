class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def slope(self, other):
        """ Returns the slope from self to other """
        if other.x == self.x:
            return 'undefined'
        return (other.y - self.y) / (other.x - self.x)

    def is_on (self, point1, point2):
        if self.slope (point1) == self.slope (point2): #if the slope between the first point and self and the second point and self is the same
            return True
        else:
            return False
        
# test cases
p = Point(0,0)
q = Point(3,6)
r = Point(1,2)
s = Point(2,3)
print(r.is_on(p,q))   # should be True
print(s.is_on(p,q))   # should be False
