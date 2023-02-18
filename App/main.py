import os
import PySimpleGUI as sg
import button
import subprocess 

sg.theme('Material2') 

# Window layout
layout = [  [sg.Text('This is the Access 3D Custom Creator (WIP)')],
            [sg.Text('Import A3D File:'), sg.FileBrowse(file_types=(("A3D Files Only", "*.A3D")),key="InputFile")],
            [sg.Text('Export STL File:'), sg.FileSaveAs(file_types=(("STL Files Only", "*.stl")),key="OutputFile")],
            [button.Rounded('Output', 0.3), button.Rounded('Cancel', 0.3)],
        ]

# Create Window
window = sg.Window('Access3D Custom Creator', layout, icon='Images\icon.ico')

# Event Loop to process 'events' and get the 'values' of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'Output':
        subprocess.Popen('openscad -o ' + values["OutputFile"] + ' -D"vartest2=5" ' + values["InputFile"])

    print('Input file: ', values["InputFile"])
    print('Output file: ', values["OutputFile"])

window.close()