import math
def distance(p1=[],p2=[]):
    vals = []
    number = 0
    num= 0
    while num < p1.count:
        vals.append(float(p2[num])-float(p1[num]))
    for value in vals:
        number +=value
    return math.sqrt(number)

