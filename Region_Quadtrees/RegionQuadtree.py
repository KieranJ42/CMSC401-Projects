class Node :
    def __init__(self, color, NW, NE, SW, SE, num) :
        self.color = color
        self.NW = NW
        self.NE = NE
        self.SW = SW
        self.SE = SE
        self.num = num

    def __str__(self) :
        retVal = "\t" + str(self.num)
        if (self.color == 0) :
            retVal += " WHITE \n"
        elif (self.color == 1) :
            retVal += " BLACK \n"
        else :
            retVal += " GRAY \n"
            retVal += self.NW.__str__()
            retVal += self.NE.__str__()
            retVal += self.SW.__str__()
            retVal += self.SE.__str__()
        return retVal


def buildTree (matrix, top, bottom, left, right, num) :
    color = matrix[top][left]
    if (bottom-top == 1) :
        return Node(color, None, None, None, None, num)
    same = True
    for i in range(top, bottom) :
        if (same==False) :
            break
        for j in range(left, right) :
            if (matrix[i][j] != color) :
                print("FIND a pixel with different value at ({},{})".format(str(j+1),str(i+1)))
                print("SPLIT block {}".format(str(num)))
                same = False
                break
    if (same) :
        return Node(color, None, None, None, None, num)
    else :
        nw = buildTree(matrix, int(top), int((top+bottom)/2), int(left), int((left+right)/2), num*4 + 1)
        ne = buildTree(matrix, int(top), int((top+bottom)/2), int((left+right)/2), int(right), num*4 + 2)
        sw = buildTree(matrix, int((top+bottom)/2), int(bottom), int(left), int((left+right)/2), num*4 + 3)
        se = buildTree(matrix, int((top+bottom)/2), int(bottom), int((left+right)/2), int(right), num*4 + 4)
        return Node (2, nw, ne, sw, se, num)

#read file into matrix of values
def buildGrid(fileContents) :
    grid = []
    line = []
    val = int(fileContents[0])
    for i in range(val) :
        for j in range(val) :
            line.append(int(fileContents[val*i + j + 1]))
        grid.append(line)
        line = []
    return grid,val

def normalBuild(grid, val) :
    print("START INPUT")
    root = buildTree(grid, 0, val, 0, val, 0)
    print("SPLIT COMPLETED\n")
    print("START RQ")
    print(root)
    print("END RQ\n")
    return root

def intersection(node1, node2) :
    returnNode = None
    if (node1.color == 0 or node2.color == 0) :
        returnNode = Node(0, None, None, None, None, node1.num)
        print("{} {} {} WHITE".format(str(node1.num), "WHITE" if node1.color==0 else 
                                ("BLACK" if node1.color==1 else "GRAY"),
                                "WHITE" if node2.color==0 else 
                                ("BLACK" if node2.color==1 else "GRAY")))
    elif (node1.color == 1) :
        returnNode = node2
        print("{} BLACK {} {}".format(str(node2.num), "WHITE" if node1.color==0 else 
                                ("BLACK" if node2.color==1 else "GRAY"),
                                "WHITE" if node2.color==0 else 
                                ("BLACK" if node2.color==1 else "GRAY")))
    elif (node2.color == 1) :
        print("{} {} BLACK {}".format(str(node1.num), "WHITE" if node1.color==0 else 
                                ("BLACK" if node1.color==1 else "GRAY"),
                                "WHITE" if node1.color==0 else 
                                ("BLACK" if node1.color==1 else "GRAY")))
        returnNode = node1
    else :
        print("{} {} {} GRAY".format(str(node1.num), "WHITE" if node1.color==0 else 
                                ("BLACK" if node1.color==1 else "GRAY"),
                                "WHITE" if node2.color==0 else 
                                ("BLACK" if node2.color==1 else "GRAY")))
        nw =  intersection(node1.NW, node2.NW)
        ne =  intersection(node1.NE, node2.NE)
        sw =  intersection(node1.SW, node2.SW)
        se =  intersection(node1.SE, node2.SE)
        if (nw.color == 0 and ne.color == 0 and sw.color == 0 and se.color == 0) :
            print("{} {} {} WHITE".format(str(node1.num), "WHITE" if node1.color==0 else 
                                ("BLACK" if node1.color==1 else "GRAY"),
                                "WHITE" if node2.color==0 else 
                                ("BLACK" if node2.color==1 else "GRAY")))
            returnNode = Node(0, None, None, None, None, node1.num)
        else :
            returnNode = Node(2, nw, ne, sw, se, node1.num)
    return returnNode

def intersectTwo(grid1, grid2, val) :
    node1 = normalBuild(grid1, val)
    node2 = normalBuild(grid2, val)
    print("START INTERSECTION")
    root = intersection(node1, node2)
    print("END INTERSECTION\n")
    print("START RQ")
    print(root)
    print("END RQ\n")

def windowClip(grid1, val, coords) :
    grid2 = []
    line = []
    for i in range(val) :
        for j in range(val) :
            if (i+1 >= int(coords[1]) and i+1 <= int(coords[3]) and j+1 >= int(coords[0]) and j+1 <= int(coords[2])) :
                line.append(1)
            else :
                line.append(0)
        grid2.append(line)
        line = []
    intersectTwo(grid1, grid2, val)


#Open file
answer = input("\nPlease enter program run type: \"Build quadtree\", \"Intersect two\", \"Window clip\", or enter \"Quit\" to quit\n")
while (answer != "Quit") :
    if (answer == "Build quadtree") :
        fileName = input("Please enter a file name\n")
        file = open(fileName,'r')
        fileContents = file.read().split()
        grid, val = buildGrid(fileContents)
        normalBuild(grid, val)
    elif (answer == "Intersect two") :
        fileName = input("Please enter first file name\n")
        file = open(fileName,'r')
        fileContents = file.read().split()
        grid1, val1 = buildGrid(fileContents)
        fileName = input("Please enter second file name\n")
        file = open(fileName,'r')
        fileContents = file.read().split()
        grid2, val2 = buildGrid(fileContents)
        if (val1 != val2) :
            print("invalid sized matrices")
        intersectTwo(grid1, grid2, val1)
    elif (answer == "Window clip") :
        fileName = input("Please enter a file name\n")
        file = open(fileName,'r')
        fileContents = file.read().split()
        grid, val = buildGrid(fileContents)
        coordStr = input("Please enter a pair of coordinates: \"[a,b],[c,d]\"\n")
        coordStr = coordStr.replace('[','')
        coordStr = coordStr.replace(']','')
        coordStr = coordStr.replace(' ','')
        coords = coordStr.split(",")
        windowClip(grid, val, coords)
    else :
        print("Invalid command provided")
    answer = input("Please enter program run type: \"Build quadtree\", \"Intersect two\", \"Window clip\", or enter \"Quit\" to quit\n")
print("Successfully exited program\n")