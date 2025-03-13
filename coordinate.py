# Coordinate Geometry
class Point:
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y
    def __str__(self):
        return f"({self.x_cod},{self.y_cod})"
    def euclidean_distance(self,other):
        return ((self.x_cod-other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    def distance_from_origin(self):
        return ((self.x_cod)**2 + (self.y_cod)**2)**0.5


class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):
        return f"{self.A}x + {self.B}y + {self.C} = 0"
    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C==0:
            return "Lies on the line"
        else:
            return "Does not lie on the line"
    def shortest_distance(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2+ line.B**2)**0.5
p1=Point(0,0)
p2=Point(1,1)
print(p1.euclidean_distance(p2))
l1=Line(1,1,-2)
print(l1.shortest_distance(p2))
