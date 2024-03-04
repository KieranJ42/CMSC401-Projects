Last updated February 8, 2024 4:21PM
Kieran Johnston: Homework 1: Point In Polygon

Function: 
    The purpose of this project is to tell whether a point is inside, outside, or on the edge of a polygon
    while also provided reasoning for why we believe it to be in such state.

Key Conventions:
    - In case 3, testing if a point is on a non-horizontal edge: 
        - rather than checking if the x-value of the point and the intersection point are equal,
        we ask if they are within a 0.000001 (1 millionth) relative error away (if the x-value of the point is not 0)
        and 0.000001 (1 millionth) absolute difference
            Ex. "1.000001 and 1" are considered the same
        in order to try to account for floating point errors
        - Example where mistake happened:
            - Run the program with polygon from testCase1 and put in the point (.435, .46) 
            - This should be an edge between vertices (0.23, 1.18) and (1.05, -1.7)
            - The intersection x-value is calculated to be 0.43500000000000005 
            - Because of this it claims the point is inside the polygon

How to use Program:
1) Run the program and when prompted write into stdin the full path to a file with a polygon definition
    Ex. write into stdin: '/Users/kieranjohnston/Desktop/Programming Projects/CMSC401/PointInPolygon/testCase1.txt'
2) You will be continually prompted for point coordinates to check if the point provided is in the polygon.
    Ex. write into stdin: '1.2 2.2'
3) To exit program, type: 'Exit' when being prompted for a point and the program will terminate

Input File Format:
    The format of the input files should be as followed:
    - First Line: A single integer, n, indicating the number of coordinates (and future lines) the polygon will contain
    - Lines 2 through n+1: Two floats seperated by a single space representing the x and y coordinates of each point
    - No extra spaces or lines should be added for accurate results

Examples: 
    To see valid files with polygon defintions, see:
        testCase1.txt
        testCase2.txt
        Personal Tests/pTest1.txt

Potential User Errors:
    - Full path of polygon definition file not provided
    - Invalid polygon definition files
        - Too few lines for what was indicated by first line of file: Error
        - Too many lines for what was indicated by first line of file: Inaccurate results
        - Single float provided in any line 2 and on: Error or inaccurate results
    - Invalid coordinate provided when prompted
