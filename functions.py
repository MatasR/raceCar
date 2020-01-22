from math import *

def collisionDetection(line1, line2): # segmentIntersect

    p0 = line1[0]
    p1 = line1[1]
    p2 = line2[0]
    p3 = line2[1]

    # Fix for the EPSILON bug
    p0 = (round(p0[0], 9), round(p0[1], 9))
    p1 = (round(p1[0], 9), round(p1[1], 9))
    p2 = (round(p2[0], 9), round(p2[1], 9))
    p3 = (round(p3[0], 9), round(p3[1], 9))

    A1 = p1[1] - p0[1]
    B1 = p0[0] - p1[0]
    C1 = A1 * p0[0] + B1 * p0[1]
    A2 = p3[1] - p2[1]
    B2 = p2[0] - p3[0]
    C2 = A2 * p2[0] + B2 * p2[1]
    denominator = A1 * B2 - A2 * B1

    # If paralel or same lines
    if(denominator == 0):
        return False

    intersectX = (B2 * C1 - B1 * C2) / denominator
    intersectY = (A1 * C2 - A2 * C1) / denominator

    if (p1[0] != p0[0]):
        rx0 = (intersectX - p0[0]) / (p1[0] - p0[0])
    else:
        rx0 = -1

    if(p1[1] != p0[1]):
        ry0 = (intersectY - p0[1]) / (p1[1] - p0[1])
    else:
        ry0 = -1

    if(p3[0] != p2[0]):
        rx1 = (intersectX - p2[0]) / (p3[0] - p2[0])
    else:
        rx1 = -1

    if(p3[1] != p2[1]):
        ry1 = (intersectY - p2[1]) / (p3[1] - p2[1])
    else:
        ry1 = -1

    if(((rx0 >= 0 and rx0 <= 1) or (ry0 >= 0 and ry0 <= 1)) and
        ((rx1 >= 0 and rx1 <= 1) or (ry1 >= 0 and ry1 <= 1))):
        return (intersectX, intersectY)
    else:
        return False

def rotatePoint2D(pointX, pointY, centerX, centerY, alpha):

    pointX = pointX - centerX
    pointY = pointY - centerY

    newX = (pointX * cos(radians(0 + alpha))) + (pointY * cos(radians(90 + alpha)))
    newY = (pointX * sin(radians(0 + alpha))) + (pointY * sin(radians(90 + alpha)))

    newX = newX + centerX
    newY = newY + centerY

    return (newX, newY)

def highscore(time):
    file = open('highscore.txt', 'r')
    highscore = file.readline()
    file.close()

    if time < float(highscore):
        file = open('highscore.txt', 'w')
        file.write(str(time))
        file.close()
        return time

    return highscore

def distance(p0, p1):
    return sqrt((p0[0]-p1[0])**2+(p0[1]-p1[1])**2)