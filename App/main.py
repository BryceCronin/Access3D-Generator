import os
import PySimpleGUI as sg
import button
import subprocess 
from pathlib import Path

sg.theme('Material2') 

# Window layout
layout = [  
    [sg.Image('Images\Logo.png')],
    [sg.Text('\nThis is the Access3D Generator (WIP)\n')],
    [sg.Text('Select A3D File:', key="text_input"), button.Rounded('Browse', 0.3, key="browse_input")],
    [sg.Text('Choose Output Folder:', key="text_output"), button.Rounded('Browse', 0.3, key="browse_output")],
    [sg.Text('')],
    [sg.Text('')],
    [button.Rounded('Generate 3D-Printable File', 0.3, key="button_export")],
]

layout_about = [
    [sg.Text('\nBuilt using Python, OpenSCAD, PySimpleGUI')],
]

# Create Window
window = sg.Window('Access3D Custom Creator', layout, icon='Images\icon.ico')

# Event Loop to process 'events' and get the 'values' of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'button_export':
        print(('openscad -o ' + file_output + os.path.basename(file_input) + ' -D"vartest2=5" ' + file_input))
        subprocess.Popen('openscad -o ' + file_output + '/' + os.path.basename(file_input)[:-4] + '_output.stl -D"vartest2=5" ' + file_input) # In future: check if file already exists, increase number if it deoes

    if event == "browse_input":
        file_input = sg.popup_get_file(
            "Select A3D File",
            file_types=((('A3D Files Only', '*.A3D'),)),
            no_window = True,
        )
        print('new browse input: ' + file_input)
        window['text_input'].update("Selected A3D File: " + os.path.basename(file_input))
        window['browse_input'].update("Change")

    if event == "browse_output":
        file_output = sg.popup_get_folder(
            "Choose Output Location",
            no_window = True,
        )
        print('new browse output: ' + file_output)  
        # window['text_output'].update("Selected Output Folder: " + os.path.basename(file_output))
        window['text_output'].update("Selected Output Folder: ..." + file_output[-20:])
        window['browse_output'].update("Change")

window.close()