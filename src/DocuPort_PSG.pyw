# #& DocuPort PSG v2.3.1-Beta
#? Simple GUI Script to open user-specified chapter of the Online-Documentation for PySimpleGUI.
#? =============================== Libraries =============================== ?#
from random import choice as rChoice
from webbrowser import open
from time import sleep as s
import PySimpleGUI as sg

#? ========================================================================= ?#
#& =============================== Functions =============================== &#

#? Changes the base color layout each time the app is opened.
theme: str = rChoice(sg.theme_list())
sg.theme(theme)


def open_PSGUI(title: str, url: str) -> bool:
    """Open a specific PySimpleGUI documentation section in the user's default browser.

    :param title: title of the documentation-section selected.
    :type title: (str)
    :param url: section URL to open in the user's default browser.
    :type url: (str)
    :returns: opens new page/tab in browser.
    :rtype: None
    """
    window_MAIN['-TEXT_TOP-'].Update(f'Opening Doc Section: {title}')
    window_MAIN.Refresh()
    return open(url, new=2, autoraise=True)


menu_choices: dict = {
    'Built-in Docs':
    sg.main_sdk_help,
    'Homepage':
    r'https://pysimplegui.readthedocs.io/en/latest/',
    'Learning Resources':
    r'https://pysimplegui.readthedocs.io/en/latest/#learning-resources',
    'Getting Started':
    r'https://pysimplegui.readthedocs.io/en/latest/#getting-started-with-pysimplegui',
    'Demo Screenshots':
    r'https://pysimplegui.readthedocs.io/en/latest/screenshots_demos',
    'Call Reference':
    r'https://pysimplegui.readthedocs.io/en/latest/call%20reference',
    'Cookbook':
    r'https://pysimplegui.readthedocs.io/en/latest/cookbook/',
    'Readme':
    r'https://pysimplegui.readthedocs.io/en/latest/readme/',
    'Popups':
    r'https://pysimplegui.readthedocs.io/en/latest/#high-level-api-calls-popups',
    'Progress Meters':
    r'https://pysimplegui.readthedocs.io/en/latest/#progress-meters',
    'Custom Windows':
    r'https://pysimplegui.readthedocs.io/en/latest/#custom-window-api-calls-your-first-window',
    'Layouts':
    r'https://pysimplegui.readthedocs.io/en/latest/#layouts',
    'Elements':
    r'https://pysimplegui.readthedocs.io/en/latest/#elements',
    'Themes':
    r'https://pysimplegui.readthedocs.io/en/latest/#themes-automatic-coloring-of-your-windows',
    'Return Values':
    r'https://pysimplegui.readthedocs.io/en/latest/#return-values',
    'System Tray':
    r'https://pysimplegui.readthedocs.io/en/latest/#systemtray',
    'Keyboard & Mouse Capture':
    r'https://pysimplegui.readthedocs.io/en/latest/#keyboard-mouse-capture',
    'Menus':
    r'https://pysimplegui.readthedocs.io/en/latest/#menus',
    'Multiple Windows':
    r'https://pysimplegui.readthedocs.io/en/latest/#running-multiple-windows',
    'Debug':
    'https://pysimplegui.readthedocs.io/en/latest/#the-pysimplegui-debugger',
    'User Settings API':
    r'https://pysimplegui.readthedocs.io/en/latest/#user-settings-api',
    'Extensions':
    r'https://pysimplegui.readthedocs.io/en/latest/#extending-pysimplegui',
    'Demo Apps':
    'https://pysimplegui.readthedocs.io/en/latest/#demo-programs-applications',
    'Create .EXE':
    r'https://pysimplegui.readthedocs.io/en/latest/#creating-a-windows-exe-file',
    'Create .MAC':
    r'https://pysimplegui.readthedocs.io/en/latest/#creating-a-mac-app-file'
}

#& ========================================================================= &#
#^ ================================ Layouts ================================ ^#
winlayout = [
    [  #* Top Row Text
        sg.Text('Choose Topic from PySimpleGUI Docs to Browse',
                key='-TEXT_TOP-',
                justification='Center')
    ],
    [  #* Option Menu & Open URL Buttons
        sg.OptionMenu(key='-OPTION_MENU-',
                      values=list(menu_choices.keys()),
                      default_value=list(menu_choices.keys())[0],
                      tooltip='Choose a topic to browse.'),
        sg.Button(
            'Open Section',
            key='-OPEN_URL-',
            tooltip=
            'Open selected section from online PySimpleGUI documentation using your default browser.'
        )
    ],
    #* Exit Button
    [sg.Exit(tooltip='Exit the program.')],
    #* Small Text to Display Current Theme
    [sg.Text(f'Current Color Theme: {theme}', font='_ 8')]
]

#~ Displays Window:
window_MAIN = sg.Window(title='DocuPort PSG',
                        layout=winlayout,
                        element_justification='Center',
                        auto_size_buttons=True,
                        keep_on_top=True,
                        element_padding=(1, 1),
                        margins=((3, 3)))
#^ ========================================================================= ^#
#* ============================= Window Events ============================= *#
while True:  #* The Infinite Loop that keeps the Window open, and returns feedback from the user.
    event, values = window_MAIN.Read()
    #print(event, values)  #NOTE: #? Enable to print stdout to console.

    #! Closes Window upon clicking 'x' or sg.Exit() Button.
    if event in [sg.WIN_CLOSED, 'Exit']:
        break
    if event == '-OPEN_URL-':
        docs_section: str = values['-OPTION_MENU-']
        if docs_section in menu_choices:
            choice = menu_choices[docs_section]
            #^ If chosen option is a function:
            if callable(choice):
                choice()
            #* If chosen option is a string:
            else:
                open_PSGUI(title=docs_section, url=choice)
                s(1.5)
                window_MAIN['-TEXT_TOP-'].Update('Done!')
                window_MAIN.Refresh()
                s(1)
    window_MAIN['-TEXT_TOP-'].Update(
        'Choose Topic from PySimpleGUI Docs to Browse')

#! Close program and release computer resources:
window_MAIN.close()
#* ========================================================================= *#
