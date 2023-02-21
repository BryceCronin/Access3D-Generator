import PySimpleGUI as sg
import button

# Theming
sg.theme('Material2') 
button_secondary_background = "#CFD8DC"
button_secondary_color = "#212121"
# Window layout
layout_settings = [
    [sg.Text('')],
]

layout_initial = [
    [sg.Text('This is the (work-in-progress) Access3D Generator App.')],
    [sg.Text('It allows you to customise 3D-printable accessibility devices to your needs.')],
    [sg.Text('Exported files are in the universal STL format - ready for 3D-printing anywhere.')],
    [sg.Text('')],
    [sg.Image('Images\inputFile.png', key="image_inputFile"), sg.Text('Select A3D File:', key="text_input"), button.Rounded('Browse', 0.3, key="browse_input")],
    [sg.Image('Images\selectFolder.png', key="image_selectFolder"), sg.Text('Select Output Folder:', key="text_output"), button.Rounded('Browse', 0.3, key="browse_output")],
    [sg.Text('')],
    [sg.Text("\nWhoops! It looks like the selected file is corrupted, please select a different A3D file and try again\n", key='invalidFile', visible=False)],
    [button.Rounded('Continue', 0.3, key="button_configure", visible=False)],
]

layout_configure = [
    # [button.Rounded('Back', 0.3, key="button_back", button_color=(button_secondary_color,button_secondary_background),mouseover_colors=(button_secondary_color,"white"))], # Do we even need a back button?
    # [button.Rounded('Test: ReadA3D', 0.3, key="button_readA3D", visible=True)], # For testing A3D file reader - remove in final app!
    [sg.Column(layout_settings, key='config_column', element_justification='l')],
    [sg.Text('')],
    [button.Rounded('Generate 3D-Printable File', 0.3, key="button_export")],
]

layout = [  
    [sg.Text('')],
    [sg.Image('Images\Logo.png')],
    [sg.Text('')],
    [sg.Column(layout_initial, key='column_initial', element_justification='c'), sg.Column(layout_configure, visible=False, key='column_configure', element_justification='c')],
    [sg.Text('')],
]