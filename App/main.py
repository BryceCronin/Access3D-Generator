import os
import PySimpleGUI as sg
import subprocess

# Theming
import button
sg.theme('Material2') 
button_secondary_background = "#CFD8DC"
button_secondary_color = "#212121"

# Window layout
layout_initial = [
    [sg.Text('This is the (work-in-progress) Access3D Generator App.')],
    [sg.Text('It allows you to customise 3D-printable accessibility devices to your needs.')],
    [sg.Text('Exported files are in the universal STL format - ready for 3D-printing anywhere.')],
    [sg.Text('')],
    [sg.Image('Images\inputFile.png', key="image_inputFile"), sg.Text('Select A3D File:', key="text_input"), button.Rounded('Browse', 0.3, key="browse_input")],
    [sg.Image('Images\selectFolder.png', key="image_selectFolder"), sg.Text('Choose Output Folder:', key="text_output"), button.Rounded('Browse', 0.3, key="browse_output")],
    [sg.Text('')],
    [sg.Text('')],
    [button.Rounded('Continue', 0.3, key="button_configure", visible=False)],
]

layout_configure = [
    [button.Rounded('Back', 0.3, key="button_back", button_color=(button_secondary_color,button_secondary_background),mouseover_colors=(button_secondary_color,"white"))],
    [sg.Text("\nPut device configuration here...\n")],
    [button.Rounded('Generate 3D-Printable File', 0.3, key="button_export")],
]

layout = [  
    [sg.Text('')],
    [sg.Image('Images\Logo.png')],
    [sg.Text('')],
    [sg.Column(layout_initial, key='column_initial', element_justification='c'), sg.Column(layout_configure, visible=False, key='column_configure', element_justification='c')],
    [sg.Text('')],
]

# Create Window
window = sg.Window('Access3D Generator', layout, icon='Images\icon.ico', element_justification='c')

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

    # Reset input/output selections
    if file_input == "":
        window['text_input'].update("Select A3D File:")
        window['browse_input'].update("Browse")
        window['image_inputFile'].update('Images\inputFile.png')
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
        # In Future:
            # Check if file already exists, increase number if it deoes
            # Make sure A3D file and output folder has been selected
        print(('openscad -o ' + file_output + os.path.basename(file_input) + ' -D"vartest2=5" ' + file_input))
        subprocess.Popen('openscad -o ' + file_output + '/' + os.path.basename(file_input)[:-4] + '_output.stl -D"vartest2=5" ' + file_input)

window.close()