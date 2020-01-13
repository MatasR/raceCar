class Point2D:
    def __init__(self):
        self.x
        self.y

    def rotatePoint(self, alpha):
        newX = (self.x * Math.cos(Math.toRadians(0 + alpha))) + (self.y * Math.cos(Math.toRadians(90 + alpha)))
        newY = (self.x * Math.sin(Math.toRadians(0 + alpha))) + (self.y * Math.sin(Math.toRadians(90 + alpha)))

        self.x = newX
        self.y = newY
