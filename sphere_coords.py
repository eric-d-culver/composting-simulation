#!/usr/bin/python3
import math

def distance(point1, point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2 + (point2[2]-point1[2])**2)

def sphere_coords(center, radius, point):
    if distance(center, point) > radius:
        return []
    else:
        res = []
        xDist = math.sqrt(radius**2 - (point[1]-center[1])**2 - (point[2] - center[2])**2)
        zDist = math.sqrt(radius**2 - (point[0]-center[0])**2 - (point[1] - center[1])**2)
        res.append((math.ceil(center[0] - xDist), point[1], point[2]))
        res.append((math.floor(center[0] + xDist), point[1], point[2]))
        res.append((point[0], point[1], math.ceil(center[2] - zDist)))
        res.append((point[0], point[1], math.floor(center[2] + zDist)))
        return res

def sphere_shell_coords(center, rad1, rad2, point):
    if distance(center, point) > rad2 or distance(center, point) < rad1:
        return []
    else:
        res = []
        return res
