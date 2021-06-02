import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image
from random import randrange, randint, uniform

import math
import time

import numpy as np
from matplotlib import pylab as plt

startTime = time.time()
distFromPoints = 3

gridSide=distFromPoints/math.sqrt(2.0)
def Point(x, y):
    return grid[x][y]

def distToPointSqrd(point1, point2):
    return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2
def isValid(pointPos):
    index = getIndexInGrid(pointPos)
    #print(index)

    if(index[0] * index[1] == 0):
        return False;
    if(index[0] >= 160 or index[1] >= 90):
        return False;
    if(index[0] < 0 or index[1] < 0):
        return False;
    if (Point(index[0], index[1]) != 0):
        return False;
    

    topLeftIndex = [index[0]-2, index[1]+2]

    for x in range(0, 5):
        for y in range(0, 5):
            ix = topLeftIndex[0]+x
            iy = topLeftIndex[1]-y
            if (ix < 0 or ix >= 159): 
                continue
                #ix=159
            if (iy < 0 or iy >= 90):
                continue
                #iy=0
            if (grid[ix][iy] != 0): 
                if( distToPointSqrd(pointPos, Point(ix, iy) ) < distFromPoints**2):
                    return False
    return True 





def randomPoint():
    x = uniform(0, 160)
    y = uniform(0, 90)
    return [truncate(x), truncate(y)]

def getIndexInGrid(point):
    #print(point)
    xCord = math.floor(point[0]/gridSide)
    yCord = math.floor(point[1]/gridSide)
    return [xCord, yCord]

def remap(value, low1, high1, low2, high2):
    return low2 + (value - low1) * (high2 - low2) / (high1 - low1)

def truncate(value):
    stepper = 10.0**3
    return math.trunc(stepper * value) / stepper


def generateSubPoint(point):
    angle = uniform(-math.pi, math.pi)#remap(randrange(0, 100), 0, 100, -math.pi, math.pi)

    vx = math.cos(angle)
    vy = math.sin(angle)
    randDistance = uniform(distFromPoints, distFromPoints*2);#remap(randrange(0, 100), 0, 100, distFromPoints, distFromPoints*2)
    return [truncate(point[0]+vx*randDistance), truncate(point[1]+vy*randDistance)]


global grid
grid = []
for x in range(0, 160):
    cell = []
    for y in range(90):
        cell.append(0)
    grid.append(cell)


firstPoint = randomPoint()
gridPos = getIndexInGrid(firstPoint)
grid[gridPos[0]][gridPos[1]] = firstPoint

activePoints = []
activePoints.append(firstPoint)


while(len(activePoints)>0):
    #print(activePoints[0])
#for i in range(0, 1000):
    pointsAdded = 0
    currentPoint = activePoints[randrange(0, len(activePoints))]
    for subPoints in range (0, 30):
        subPt = generateSubPoint(currentPoint)
        if(isValid(subPt)):
            activePoints.append(subPt)
            ptCoords = getIndexInGrid(subPt)
            grid[ptCoords[0]][ptCoords[1]]=subPt
            pointsAdded += 1 
    if pointsAdded == 0:
        activePoints.remove(currentPoint)


xCoords = list();
yCoords = list();
for x in range(0, 160):
    for y in range(0, 90):
        if(grid[x][y] != 0):
            xCoords.append(Point(x, y)[0])
            yCoords.append(Point(x, y)[1])

plt.plot(xCoords, yCoords, linestyle="None", marker="o", color="r")
plt.title("Croissant Disc Sampling", fontsize=19)
plt.xlim(0, 160)
plt.ylim(0, 90)
plt.gca().set_aspect('equal', adjustable='box')
#plt.gca().set_facecolor((.1, .1, .1))
#plt.patch.set_facecolor((0, 0, 0))
executionTime = time.time() - startTime
print(f"Finished Executing in {truncate(executionTime)}s")
plt.show()    
#plt.savefig('lissajous.png', bbox_inches='tight')





#print("getToTheEnd")
