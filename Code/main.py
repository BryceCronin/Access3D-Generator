import os
import PySimpleGUI as sg
import button


# msg = "Testing os, maybe used for customising OpenSCAD files?"
# print(msg)
# print(os.popen("ipconfig").read())

sg.theme('Material2') 
# All the stuff inside your window.
layout = [  [sg.Text('This is the Access 3D Custom Creator (WIP)')],
            [sg.Text('Import File:'), sg.InputText()],
            [button.Rounded('Ok', 0.3), button.Rounded('Cancel', 0.3)]]

# Create the Window
window = sg.Window('Access3D Custom Creator', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()