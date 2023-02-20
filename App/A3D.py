A3D_start = -1 # Line number of A3D-Start
A3D_end = - 1 # Line number of A3D-End
A3D_file = 0
A3D_lines = 0

def initiateFile (filePath):
    global A3D_start
    global A3D_end
    global A3D_file
    global A3D_lines
    A3D_file = ((open(filePath)))
    A3D_lines = (A3D_file.readlines()) # Each line in a list
    A3D_lineCount = len(A3D_lines) # Number of lines
    
    # Get Line number of A3D-Start
    for x in range(A3D_lineCount):
        search = A3D_lines[x].find("A3D-Start")
        if search != -1:
            A3D_start = x
            break
        else:
            A3D_start = -1

    # Get Line number of A3D-End
    for x in range(A3D_lineCount):
        search = A3D_lines[x].find("A3D-End")
        if search != -1:
            A3D_end = x
            break
        else:
            A3D_end = -1

    if ((A3D_end != -1) and (A3D_start != -1)):
        return True # Valid A3D file
    else:
        return False # Invalid A3D file
    
def getStart():
    return A3D_start

def getEnd():
    return A3D_end

def extractFields(start,end):
    # todo: convert each line of the A3D notation into buttons on the form
    print("EXTRACTING FIELDS START")
    for x in range(start+1,end):
        print(A3D_lines[x])
        