Last updated March 4, 2024 4:47PM
Kieran Johnston: Homework 2: Representing Raster Images thorugh Region Quadtrees

Function: 
    The purpose of this project is to buildm and efficiently store binary "images" through the implementation
    of quadtrees. These quadtrees should also have the capabilities to perform certain set operations
    on them (right now just intersection)

Key Conventions:
    - During each instance of inputting a "program run type" you will have to put in filenames for quadtree
        generation. This means, quadtrees won't be stored/saved after each round

How to use Program:
1) Run the program and when prompted for a "program run type" enter either:
    "Build quadtree" to test building a normal quadtree
    "Intersect two" to test intersecting 2 equal sized quadtrees
    "Window clip" to test window clippling of a quadtree
    "Quit" to terminate program
2) Run the program and when prompted write into stdin the full path to a file with a quadtree definition
    Ex. write into stdin: '/Users/kieranjohnston/Desktop/Programming Projects/CMSC401/Region_Quadtrees/myCase1.txt'
    2a) "Build quadtree" will be done after this
    2b) "Intersect two" will then prompt for a second file (same format) (sizes of quadtrees must also be the same)
    2c) "Window clip" will then prompt for a pair of integer coordinates 
        for integers a,b,c,d write into stdin: '[a,b],[c,d]'
4) To exit program, type: 'Quit' when being prompted for a program run type and the program will terminate

Input File Format:
    The format of the input files should be as followed:
    - First Line: A single integer, n (such that n = 2^k for an integer k), indicating the side length of the matrix
    - Lines 2 through n+1: space seperated list of n 0 or 1's
    - No extra spaces or lines should be added for accurate results

Examples: 
    To see valid files with polygon defintions, see:
        myCase1.txt
        myCase2.txt
        givenCase1.txt
        givenCase2.txt

Potential User Errors:
    - Full path of quadtree definition file not provided
    - Invalid quadtree definition files
        - Too few lines for what was indicated by first line of file: Error
        - Too many lines for what was indicated by first line of file: Inaccurate results
        - A number other than 0 or 1 provided in any line 2 and on: Error or inaccurate results
    - Invalid file or pair of coordinates provided when prompted
