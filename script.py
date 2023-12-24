import PySimpleGUI as sg

def count_words(text):
    text = text.strip()
    if not text:
        return 0
    words = text.split()  # Split the text into words
    return len(words)

layout = [
    [sg.Text('Enter text to count words:')],
    [sg.Multiline(size=(50, 5), key='-Text-')],
    [sg.Button('Count Words'), sg.Exit()]
]

window = sg.Window('Word Counter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Count Words':
        text_input = values['-Text-']
        word_count = count_words(text_input)
        sg.popup(f'The number of words in the text is: {word_count}')

window.close()
