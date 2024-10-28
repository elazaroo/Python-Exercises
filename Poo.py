import math

class Dot():
    # Constructors
    def __init__(self, x=0, y=0, d=None):
        if isinstance(d, Dot):
            self.x = d.x
            self.y = d.y
        else:
            self.x  = x
            self.y = y

    # Getters and Setters
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get(self):
        return self.x, self.y
    
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
    
    def set(self, x, y):
        self.x = x
        self.y = y

    # Functions
    def distance(self, dot):
        return (self.x - dot.x), (self.y - dot.y)
    
    def distance(self, x, y):
        return (self.x - x), (self.y -y)

    @staticmethod
    def distance(d1, d2):
        return (d1.x - d2.x), (d1.y - d2.y)
    
    def traslade(self, vector):
        self.x += vector.x
        self.y += vector.y

    def print(self):
        print("(" + self.x + ", " +  self.y+ ")")

class Vector():
    # Constructors
    def __init__(self, ox=0, oy=0, dot1=None, dot2=None, vector=None):
        if isinstance(dot1, Dot) and isinstance(dot2, Dot):
            self.ox = (dot1.x + dot2.x)
            self.oy = (dot1.y + dot2.y)
        elif isinstance(vector, Vector):
            self.ox = vector.ox
            self.oy = vector.oy
        else:
            self.ox = ox
            self.oy = oy

    # Getters and Setters
    def get_ox(self):
        return self.ox
    
    def get_oy(self):
        return self.oy
    
    def get(self):
        return self.ox, self.oy
    
    def set_ox(self, ox):
        self.ox = ox

    def set_oy(self, oy):
        self.oy = oy

    def set(self, ox, oy):
        self.ox = ox
        self.oy = oy
    
    # Functions
    def print(self):
        print("[" + self.ox + ", " + self.oy + "]")

class Circle():
    # Constructors
    def __init__(self, center=0, radius=0, circle=None):
        if isinstance(circle, Circle):
            self.center = circle.center
            self.radius = circle.radius
        else:
            self.center = center
            self.radius = radius

    # Getters and Setters
    def get_center(self):
        return self.center
    
    def get_radius(self):
        return self.radius
    
    def get(self):
        return self.center, self.radius
    
    def set_center(self, center):
        self.center = center

    def set_radius(self, radius):
        self.radius = radius

    def set(self, center, radius):
        self.center = center
        self.radius = radius
        
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def traslade(self, vector=None):
        self.center = Dot(self.center.x + vector.ox, self.center.y + vector.oy)

    def scale(self, factor):
        self.radius *= factor

    def print(self):
        print("{(" + self.center.x + ", " + self.center.y + "), " + self.radius + "}")