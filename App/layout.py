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
    [sg.Text('')],
    [sg.Image('Images\Logo.png')],
    [sg.Text('')],
    [sg.Text('This is the Access3D Generator App.')],
    [sg.Text('It allows you to customise 3D-printable accessibility devices to your needs.')],
    [sg.Text('Exported files are in the universal STL format - ready for 3D-printing anywhere.')],
    [sg.Text('')],
    [sg.Image('Images\inputFile.png', key="image_inputFile"), sg.Text('Select A3D File:', key="text_input"), button.Rounded('Browse', 0.3, key="browse_input")],
    [sg.Image('Images\selectFolder.png', key="image_selectFolder"), sg.Text('Select Output Folder:', key="text_output"), button.Rounded('Browse', 0.3, key="browse_output")],
    [sg.Text('')],
    [sg.Text("\nWhoops! It looks like the selected file is corrupted, please select a different A3D file and try again\n", key='invalidFile', visible=False)],
    [button.Rounded('Continue', 0.3, key="button_configure", visible=False)],
]

layout_configure_right = [
    [sg.Image('Images\Logo_sm.png')],
    [sg.Column(layout_settings, key='config_column', element_justification='l')],
    [sg.Text('')],
    [button.Rounded('Update Preview', 0.3, key="button_update", button_color=(button_secondary_color,button_secondary_background),mouseover_colors=(button_secondary_color,"white")),button.Rounded('Export 3D File', 0.3, key="button_export")],
]

layout_configure_left = [
    [sg.Image('Images\previewPanel_l.png', pad=((15,0),0)), sg.Column(layout=[[sg.Canvas(key='fig_cv',size=(500, 400))]],background_color='#FFFFFF',p=0), sg.Image('Images\previewPanel_r.png', pad=((0,10), 0))],
]

layout_configure = [
    [sg.Column(layout_configure_left, vertical_alignment='center', element_justification='c'), sg.Column(layout_configure_right, vertical_alignment='center', element_justification='c')],
]

layout = [  
    [sg.Text('')],
    [sg.Column(layout_initial, key='column_initial', element_justification='c'), sg.Column(layout_configure, visible=False, key='column_configure', element_justification='c')],
    [sg.Text('')],
]