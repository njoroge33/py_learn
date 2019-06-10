# Create a class called Point that includes two instance variables - x(type int) and y(type int) 
# Provide a constructor that initializes the two instance variables 
# Provide decideQuadrant() method in the Point class 
# The method should return which quadrant of x/y this Point object falls in 
# Quadrant 1 contains all points whose x and y values are both positive 
# Quadrant 2 contains all points with negative x but positive y 
# Quadrant 3 contains all points with negative x and y values 
# Quadrant 4 contains all points with positive x but negative y 
# If the point lies directly on x and/or y axis return 0 
# Create a Point object and display object's quadrant 
# for more info on this quiz, go to this url: http://www.programmr.com/quadrant-point-2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def decide_quadrant(self):
        x = self.x
        y = self.y
        if  x > 0 and y > 0:
            return "Quadrant 1"
        if  x < 0 and y > 0:
            return "Quadrant 2"
        if  x < 0 and y < 0:
            return "Quadrant 3"
        if  x > 0 and y < 0:
            return "Quadrant 4"
        else:
            return 0


points = Point(4, 2)

print(points.decide_quadrant())
