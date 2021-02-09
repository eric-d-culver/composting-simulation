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
        x2Dist = math.sqrt(rad2**2 - (point[1]-center[1])**2 - (point[2] - center[2])**2)
        z2Dist = math.sqrt(rad2**2 - (point[0]-center[0])**2 - (point[1] - center[1])**2)
        x1DistSq = rad1**2 - (point[1] - center[1])**2 - (point[2] - center[2])**2
        z1DistSq = rad1**2 - (point[0] - center[0])**2 - (point[1] - center[1])**2
        if x1DistSq < 0:
            res.append((math.ceil(center[0] - x2Dist), point[1], point[2]))
            res.append((math.floor(center[0] + x2Dist), point[1], point[2]))
        else:
            res.append((math.ceil(center[0] - x2Dist), point[1], point[2]))
            res.append((math.floor(center[0] - math.sqrt(x1DistSq)), point[1], point[2]))
            res.append((math.ceil(center[0] + math.sqrt(x1DistSq)), point[1], point[2]))
            res.append((math.floor(center[0] + x2Dist), point[1], point[2]))
        if z1DistSq < 0:
            res.append((point[0], point[1], math.ceil(center[2] - z2Dist)))
            res.append((point[0], point[1], math.floor(center[2] + z2Dist)))
        else:
            res.append((point[0], point[1], math.ceil(center[2] - z2Dist)))
            res.append((point[0], point[1], math.floor(center[2] - math.sqrt(z1DistSq))))
            res.append((point[0], point[1], math.ceil(center[2] + math.sqrt(z1DistSq))))
            res.append((point[0], point[1], math.floor(center[2] + z2Dist)))
        return res

def pretty_print_test(center, rad1, rad2, point):
    print("center:", center)
    print("From", rad1, "to", rad2)
    print("At", point)
    print(sphere_shell_coords(center, rad1, rad2, point))

pretty_print_test((24, 37, 164), 24, 32, (1, 46, 160))
pretty_print_test((24, 37, 164), 24, 32, (1, 46, 180))
