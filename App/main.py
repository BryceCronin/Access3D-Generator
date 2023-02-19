import os
import PySimpleGUI as sg
import subprocess
import button
import layout

# Create Window
window = sg.Window('Access3D Generator', layout.layout, icon='Images\icon.ico', element_justification='c')

# Initiate variables
file_input = ""
file_output = ""

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
            file_input = selected
            print('new browse input: ' + file_input)
            window['text_input'].update("Selected A3D File: " + os.path.basename(file_input))
            window['browse_input'].update("Change")
            window['image_inputFile'].update('Images\inputFile_done.png')
    if file_input == "":
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
        window['text_output'].update("Choose Output Folder:")
        window['browse_output'].update("Browse")
        window['image_selectFolder'].update('Images\selectFolder.png')

    # Continue to configure
    if file_input != "" and file_output != "":
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
        # In Future: Check if file already exists, increase number if it deoes
        print(('openscad -o ' + file_output + os.path.basename(file_input) + ' -D"vartest2=5" ' + file_input))
        subprocess.Popen('openscad -o ' + file_output + '/' + os.path.basename(file_input)[:-4] + '_output.stl -D"vartest2=5" ' + file_input)

window.close()