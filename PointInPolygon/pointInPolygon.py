def intersect_Edge(point, edge) :
    #case 1: point to right of edge
    if (point[0]>edge[0][0] and point[0]>edge[1][0]) :
        return 0
    #case 2: edge is horizontal and either is not vertically aligned or 
    if (edge[0][1] == edge[1][1]) :
        #not vertically aligned    or    point is fully to the left of the edge
        if (point[1] != edge[0][1] or (point[0]<edge[0][0] and point[0]<edge[1][0])) :
            return 0
        else : #On the line
            return -1
    #case 3-5: Other intersections
        #((yp - y1) / (y2 - y1)) * (x2 - x1) + x1
    intPoint = ((point[1]-edge[0][1]) / (edge[1][1]-edge[0][1])) * (edge[1][0]-edge[0][0]) + edge[0][0]
    #3: on edge 
    if (((point[0]==0 or abs(1-intPoint/point[0]) < 0.000001)) and (abs(intPoint-point[0]) < 0.000001)) and ((point[1]<=edge[0][1] and point[1]>=edge[1][1]) or (point[1]>=edge[0][1] and point[1]<=edge[1][1])) :
        return -1
    #4: intersection point is an endpoint
    #4a: intersection is 1st endpoint
    if (point[0] < edge[0][0]) and (point[1] == edge[0][1]) :
        if (edge[0][1] < edge[1][1]) :
            return 1 #1st endpoint is low value
        #else 1st endpoint is high value: return 0
    #if x coord of point > 1st endpoint => No intersection: return 0

    #4b: intersection is 2nd endpoint
    if (point[0] < edge[1][0]) and (point[1] == edge[1][1]) :
        if (edge[1][1] < edge[0][1]) :
            return 1 #2nd endpoint is low value
        #else 2nd endpoint is high value: return 0
    #if x coord of point > 2nd endpoint => No intersection: return 0

    #5: intersection point inside edge
    if (intPoint > point[0]) and ((point[1]<edge[0][1] and point[1]>edge[1][1]) or (point[1]>edge[0][1] and point[1]<edge[1][1])) :
        return 1 #Intersection
    else :
        return 0 #No Intersection


#Open file
fileName = input("Please enter file name\n")
file = open(fileName,'r')
fileContents = file.read().split()

#Store file contents in list of points
polygon = []
for i in range(int(fileContents[0])) :
    polygon.append((float(fileContents[2*i+1]),float(fileContents[2*i+2])))

#Ask for points and check whether points are in the polygon
point = input("Please enter a point\n")
intersections = 0
ret_val = 0 #1: in the polygon, 0: not in the polygon, -1 On the edge of the polygon
while point != "Exit" :
    coordStr = point.split()
    intersections = 0
    ret_val = 0
    coordinate = (float(coordStr[0]),float(coordStr[1]))
    print("Polygon PL: " + str(polygon) + "\n\nPoint P: " + str(coordinate) + "\n\nIs P in PL?")
    for i in range (int(fileContents[0])) :
        temp = intersect_Edge(coordinate,(polygon[i],polygon[(i+1)%int(fileContents[0])]))
        print ("Edge " + str((polygon[i],polygon[(i+1)%int(fileContents[0])])) + ", intersection: " + str((temp+3)%3))
        if (temp == -1) :
            ret_val = -1 #On an edge marker
        intersections += temp
    if (ret_val != -1) :
        ret_val = intersections % 2
    if (ret_val == -1) :
        print("On edge\n")
    if (ret_val == 0) :
        print("Outside\n")
    if (ret_val == 1) :
        print("Inside\n")
    point = input("Please enter another point or 'Exit' to finish\n")

print("Successfully exited\n")