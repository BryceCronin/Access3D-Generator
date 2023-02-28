import re
import PySimpleGUI as sg
import layout

A3D_start = -1 # Line number of A3D-Start
A3D_end = - 1 # Line number of A3D-End
A3D_file = 0
A3D_lines = 0
fieldList = []

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
    global fieldList
    
    for x in range(start+1,end):
        # Put current items into a list (type,title,desc)
        currentList = []
        currentList.clear()
        currentList.append(re.findall(r'\[.*?\]', A3D_lines[x])) # variable
        currentList.append(re.findall(r'\<.*?\>', A3D_lines[x])) # name
        currentList.append(re.findall(r'\{.*?\}', A3D_lines[x])) # description
        if A3D_lines[x].__contains__("Boolean"):
            currentList.append('boolean')
        elif A3D_lines[x].__contains__("Integer"):
            currentList.append('integer')
        # Then add list to list of list
        fieldList.append(currentList)
    
    return(fieldList)

def formatString(str):
    # Removes the ['( characters from front and end of string
    newString = str[3:]
    newString = newString[:-3]
    return newString