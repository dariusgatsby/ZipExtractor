import PySimpleGUI as sg
from unzip import extractor

folder_label = sg.Text("Select file to extract:")
folder_button = sg.FileBrowse("Choose", key='folder')
folder_input = sg.Input()

extract_label = sg.Text("Select extract location:")
extract_button = sg.FolderBrowse("Choose", key='extract')
extract_input = sg.Input()
extract_success = sg.Text('', key='message')

convert_button = sg.Button("Convert")

layout = [[folder_label, folder_input, folder_button],
          [extract_label, extract_input, extract_button],
          [convert_button, extract_success]]
font = ('Arial', 15)

window = sg.Window('Zip Extractor', layout=layout, font=font)
while True:
    events, values = window.read()
    print(events, values)
    if events == "Convert":
        folder_to_unzip = values['folder']
        extract_loc = values['extract']
        extractor(folder_to_unzip, extract_loc)
        window['message'].update(value='Extraction Successful!')
    elif events == "WIN_CLOSED":
        break

window.close()
