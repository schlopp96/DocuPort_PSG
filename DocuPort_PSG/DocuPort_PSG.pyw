#!/usr/bin/env python3

#! Simple GUI Script to open user-specified chapter of the Online-Documentation for PySimpleGUI.
#@ =============================== Libraries =============================== @#
from random import choice as rChoice
from webbrowser import open
from time import sleep as s
import PySimpleGUI as sg

#@ ========================================================================= @#
#$ =============================== Functions =============================== $#

__version__ = '2.3.3b'

#> Changes the base color layout each time the app is opened.
rtheme: str = rChoice(sg.theme_list())
sg.theme(rtheme)


def open_PSGUI(url: str) -> bool:
    """Open a specific PySimpleGUI documentation section in the user's default browser.

    ---
    Parameters
        :param url: URL of the doc-section to open in user's default browser.
        :type url: str
        :return: opens new page/tab in browser.
        :rtype: None
    """
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
    r'https://pysimplegui.readthedocs.io/en/latest/#the-pysimplegui-debugger',
    'User Settings API':
    r'https://pysimplegui.readthedocs.io/en/latest/#user-settings-api',
    'Extensions':
    r'https://pysimplegui.readthedocs.io/en/latest/#extending-pysimplegui',
    'Demo Apps':
    r'https://pysimplegui.readthedocs.io/en/latest/#demo-programs-applications',
    'Create .EXE':
    r'https://pysimplegui.readthedocs.io/en/latest/#creating-a-windows-exe-file',
    'Create .MAC':
    r'https://pysimplegui.readthedocs.io/en/latest/#creating-a-mac-app-file'
}

#& ========================================================================= &#
#> ================================ Layouts ================================ <#
winlayout = [
    [
        sg.Text('Choose Topic from PySimpleGUI Docs to Browse',
                key='-TEXT_TOP-',
                justification='Center')
    ],
    [
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
    ], [sg.Exit(tooltip='Exit the program.')],
    [sg.Text(f'Current Color Theme: {rtheme}', font='_ 8')]
]

#@ Displays Window:
window_MAIN = sg.Window(title='DocuPort - PySimpleGUI',
                        layout=winlayout,
                        element_justification='Center',
                        auto_size_buttons=True,
                        auto_size_text=True,
                        keep_on_top=True,
                        element_padding=(1, 1),
                        margins=((3, 3)))


#> ========================================================================= <#
#$ ============================= Window Events ============================= $#
def main():
    while True:
        event, values = window_MAIN.read()
        print(event, values
              )  #NOTE: #? Enable to print stdout to console. #DEFAULT: -> OFF

        #@ Closes Window upon clicking 'x' or sg.Exit() Button.
        if event in [sg.WIN_CLOSED, 'Exit']:
            break
        if event == '-OPEN_URL-':
            docs_section: str = values['-OPTION_MENU-']
            if docs_section in menu_choices:
                choice = menu_choices[docs_section]

                #> If chosen option is a valid function:
                if callable(choice):
                    choice()  #< Call chosen function.

                #* If chosen option is a string variable:
                else:
                    open_PSGUI(url=choice)
                    window_MAIN['-TEXT_TOP-'].update(
                        f'Opening Doc Section: {docs_section}')
                    window_MAIN.refresh()
                    s(1.5)
                    window_MAIN['-TEXT_TOP-'].update('Done!')
                    window_MAIN.Refresh()
                    s(1)
        window_MAIN['-TEXT_TOP-'].update(
            'Choose Topic from PySimpleGUI Docs to Browse')

    window_MAIN.close()


if __name__ == '__main__':
    main()

#$ ========================================================================= $#
