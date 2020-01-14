from math import *

def rotatePoint2D(pointX, pointY, centerX, centerY, alpha):

    pointX = pointX - centerX
    pointY = pointY - centerY

    newX = (pointX * cos(radians(0 + alpha))) + (pointY * cos(radians(90 + alpha)))
    newY = (pointX * sin(radians(0 + alpha))) + (pointY * sin(radians(90 + alpha)))

    newX = newX + centerX
    newY = newY + centerY

    return newX, newY