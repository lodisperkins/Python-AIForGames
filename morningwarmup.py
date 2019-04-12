import math
def distance(p1=[],p2=[]):
    vals = []
    number = 0
    num= 0
    for num in range [0,p1.count]:
        vals.append(float(p2[num])-float(p1[num]))
    for value in vals:
        number +=value
    return math.sqrt(number)
def insidebox(pos,rect):
    if pos.X>rect.topleft.X and pos.Y < rect.topleft.Y and pos.X < rect.bottomright.X and pos.Y > rect.bottomright.Y:
        return true
point1 =[]
point1.append(1)
point1.append(2)
point1.append(3)
point2 = []
point2.append(4)
point2.append(5)
point2.append(6)
print (distance(point1,point2))
