import math

def regular_polygon(perimeter, vertices):
    side = perimeter/vertices
    angle = (vertices-2)*180/vertices
    height = side/2*math.tan(math.radians(angle/2))
    area = 1/2*side*height*vertices
    return area
