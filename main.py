import PySimpleGUI as sg

folder_label = sg.Text("Select file to extract:")
folder_button = sg.Button("Choose")
folder_input = sg.Input(key='folder')

extract_label = sg.Text("Select extract location:")
extract_button = sg.Button("Choose")
extract_input = sg.Input(key='extract')

convert_button = sg.Button("Convert")

layout = [[folder_label, folder_input, folder_button],
          [extract_label, extract_input, extract_button],
          [convert_button]]
font = ('Arial', 15)

window = sg.Window('Zip Extractor', layout=layout, font=font)
while True:
    events, values = window.read()

window.close()
