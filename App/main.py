import os
import PySimpleGUI as sg
import button
import subprocess 

sg.theme('Material2') 

# Window layout
layout = [  [sg.Text('This is the Access 3D Custom Creator (WIP)')],
            [sg.Text('Import File:'), sg.FileBrowse()],
            [sg.Text('Export file name:'), sg.InputText()],
            [button.Rounded('Ok', 0.3), button.Rounded('Cancel', 0.3)],
            [button.Rounded('Output file test', 0.3), button.Rounded('ls', 0.3)], # for testing
        ]

# Create Window
window = sg.Window('Access3D Custom Creator', layout, icon='Images\icon.ico')

# Event Loop to process 'events' and get the 'values' of the inputs
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'Output file test':
        subprocess.Popen('openscad -o Output/'+values[0]+'.stl -D"vartest2=5" Input/Test.3PA')
        print("did the thing")

    if event == 'ls':
        print(os.listdir())

    print('Output file name: ', values[0])

window.close()