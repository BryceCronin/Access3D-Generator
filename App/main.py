import os
import PySimpleGUI as sg
import subprocess
import layout
import datetime
import A3D

# Create Window
window = sg.Window('Access3D Generator', layout.layout, icon='Images\icon.ico', element_justification='c')

# Initiate variables
file_input = ""
file_output = ""
file_valid = True

# Event Loop to process 'events' and get the 'values' of the inputs
while True:
    event, values = window.read()

    # Close App
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    # Input A3D File
    if event == "browse_input":
        selected = sg.popup_get_file(
            "Select A3D File",
            file_types=((('A3D Files Only', '*.A3D'),)),
            no_window = True,
            history=True )
        if selected != "":
            if (A3D.initiateFile(selected) == True): # Valid A3D file
                file_input = selected
                if file_input != "" and file_output != "":
                    window['button_configure'].update(visible=True)
                print('new browse input: ' + file_input)
                window['invalidFile'].update(visible=False)
                window['text_input'].update("Selected A3D File: " + os.path.basename(file_input))
                window['browse_input'].update("Change")
                window['image_inputFile'].update('Images\inputFile_done.png')
                file_valid = True
            else: # Invalid A3D file
                file_input = selected
                window['button_configure'].update(visible=False)
                window['invalidFile'].update(visible=True)
                window['text_input'].update("Invalid A3D File: " + os.path.basename(file_input))
                window['browse_input'].update("Replace")
                window['image_inputFile'].update('Images\inputFile_error.png')
                file_valid = False
    if file_input == "" and file_valid == True:
        window['text_input'].update("Select A3D File:")
        window['browse_input'].update("Browse")
        window['image_inputFile'].update('Images\inputFile.png')
        
    # Select Output Location
    if event == "browse_output":
        selected = sg.popup_get_folder(
            "Choose Output Location",
            no_window = True, )
        if selected != "":
            file_output = selected
            print('new browse output: ' + file_output)  
            window['text_output'].update("Selected Output Folder: ..." + file_output[-20:])
            window['browse_output'].update("Change")
            window['image_selectFolder'].update('Images\selectFolder_done.png')
    if file_output == "":
        window['text_output'].update("Select Output Folder:")
        window['browse_output'].update("Browse")
        window['image_selectFolder'].update('Images\selectFolder.png')

    # Continue to configure
    if file_input != "" and file_output != "" and file_valid == True:
        window['button_configure'].update(visible=True)
    if event == 'button_configure':
        window['column_initial'].update(visible=False)
        window['column_configure'].update(visible=True)

    # Return to initial
    if event == 'button_back':
        window['column_initial'].update(visible=True)
        window['column_configure'].update(visible=False)

    # Export STL File
    if event == 'button_export':
        outputFile = (file_output + '/' + os.path.basename(file_input)[:-4] + '.stl')
        if (os.path.isfile(outputFile)):
            outputFile = (file_output + '/' + os.path.basename(file_input)[:-4] + '_' + ((datetime.datetime.now()).strftime("%H %M %S")).replace(" ","-") )
        openScadString = ('openscad -o ' + outputFile + '_output.stl -D"vartest2=5" ' + file_input)
        print(openScadString )
        subprocess.Popen(openScadString)

    # Read A3D File
    if event == 'button_readA3D':
        A3D.initiateFile(file_input)
        list = A3D.extractFields(A3D.getStart(),A3D.getEnd())
        # print(str((A3D.extractFields(A3D.getStart(),A3D.getEnd()))[1][1]))
        for x in range(len(list)):
            for y in range(len(list[x])):
                window.extend_layout(window['config_column'], [[sg.Text(str((A3D.extractFields(A3D.getStart(),A3D.getEnd()))[x][y]))]])

window.close()

