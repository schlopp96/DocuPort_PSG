# #& DocuPort PSG v2.0.1-Beta
#? Simple GUI Script to open user-specified chapter of the Online-Documentation for PySimpleGUI.

from random import choice as rChoice
from time import sleep as s
from webbrowser import open

import PySimpleGUI as sg


def randomTheme():
    """Randomizes Program Color Theme on Launch.
    
    - Includes EVERY* available default theme by simply calling a random-choice funcion to pick from a list.
        - *I removed the "SystemDefault", "SystemDefault1", and "SystemDefaultForRealThisTime" themes.
    """
    themeChoices = [
        'Black',
        'BlueMono',
        'BluePurple',
        'BrightColors',
        'BrownBlue',
        'Dark',
        'Dark2',
        'DarkAmber',
        'DarkBlack',
        'DarkBlack1',
        'DarkBlue',
        'DarkBlue1',
        'DarkBlue10',
        'DarkBlue11',
        'DarkBlue12',
        'DarkBlue13',
        'DarkBlue14',
        'DarkBlue15',
        'DarkBlue16',
        'DarkBlue17',
        'DarkBlue2',
        'DarkBlue3',
        'DarkBlue4',
        'DarkBlue5',
        'DarkBlue6',
        'DarkBlue7',
        'DarkBlue8',
        'DarkBlue9',
        'DarkBrown',
        'DarkBrown1',
        'DarkBrown2',
        'DarkBrown3',
        'DarkBrown4',
        'DarkBrown5',
        'DarkBrown6',
        'DarkBrown7',
        'DarkGreen',
        'DarkGreen1',
        'DarkGreen2',
        'DarkGreen3',
        'DarkGreen4',
        'DarkGreen5',
        'DarkGreen6',
        'DarkGreen7',
        'DarkGrey',
        'DarkGrey1',
        'DarkGrey10',
        'DarkGrey11',
        'DarkGrey12',
        'DarkGrey13',
        'DarkGrey14',
        'DarkGrey2',
        'DarkGrey3',
        'DarkGrey4',
        'DarkGrey5',
        'DarkGrey6',
        'DarkGrey7',
        'DarkGrey8',
        'DarkGrey9',
        'DarkPurple',
        'DarkPurple1',
        'DarkPurple2',
        'DarkPurple3',
        'DarkPurple4',
        'DarkPurple5',
        'DarkPurple6',
        'DarkPurple7',
        'DarkRed',
        'DarkRed1',
        'DarkRed2',
        'DarkTanBlue',
        'DarkTeal',
        'DarkTeal1',
        'DarkTeal10',
        'DarkTeal11',
        'DarkTeal12',
        'DarkTeal2',
        'DarkTeal3',
        'DarkTeal4',
        'DarkTeal5',
        'DarkTeal6',
        'DarkTeal7',
        'DarkTeal8',
        'DarkTeal9',
        'Default',
        'Default1',
        'DefaultNoMoreNagging',
        'Green',
        'GreenMono',
        'GreenTan',
        'HotDogStand',
        'Kayak',
        'LightBlue',
        'LightBlue1',
        'LightBlue2',
        'LightBlue3',
        'LightBlue4',
        'LightBlue5',
        'LightBlue6',
        'LightBlue7',
        'LightBrown',
        'LightBrown1',
        'LightBrown10',
        'LightBrown11',
        'LightBrown12',
        'LightBrown13',
        'LightBrown2',
        'LightBrown3',
        'LightBrown4',
        'LightBrown5',
        'LightBrown6',
        'LightBrown7',
        'LightBrown8',
        'LightBrown9',
        'LightGray1',
        'LightGreen',
        'LightGreen1',
        'LightGreen10',
        'LightGreen2',
        'LightGreen3',
        'LightGreen4',
        'LightGreen5',
        'LightGreen6',
        'LightGreen7',
        'LightGreen8',
        'LightGreen9',
        'LightGrey',
        'LightGrey1',
        'LightGrey2',
        'LightGrey3',
        'LightGrey4',
        'LightGrey5',
        'LightGrey6',
        'LightPurple',
        'LightTeal',
        'LightYellow',
        'Material1',
        'Material2',
        'NeutralBlue',
        'Purple',
        'Python',
        'Reddit',
        'Reds',
        'SandyBeach',
        'SystemDefault',
        'Tan',
        'TanBlue',
        'TealMono',
        'Topanga',
    ]
    return rChoice((themeChoices))


#? Changes the base color layout each time the app is opened.
sg.theme(randomTheme())


def open_PSGUI(
    title: str,
    url: str,
) -> bool:
    """Open a specific PySimpleGUI documentation section in the user's default browser.
    
    :param title: | title of the documentation-section selected.
    :param url: | section URL to open in the user's default browser.
    
    :rtype: (bool)
    """
    url = fr'{url}'
    window_MAIN['-TEXT_TOP-'].update(f'Opening Page: {title}')
    window_MAIN.refresh()
    s(1)
    return open(url, new=2, autoraise=True)


winlayout = [
    [  #* Top Row Text
        sg.Text(
            'Choose a Chapter/Section of the PySimpleGUI Documentation to Browse',
            auto_size_text=True,
            key='-TEXT_TOP-')
    ],
    [  #* Option Menu & Open URL Buttons
        sg.OptionMenu(
            key='-OPTION_MENU-',
            values=[
                'Homepage', 'Learning Resources', 'Getting Started',
                'Demo Screenshots', 'Call Reference', 'Cookbook', 'Readme',
                'Popups', 'Progress Meters', 'Custom Windows', 'Layouts',
                'Elements', 'Themes', 'Return Values', 'System Tray',
                'Keyboard & Mouse Capture', 'Menus', 'Multiple Windows',
                'Debug', 'User Settings API', 'Extensions', 'Demo Apps',
                'Create .EXE', 'Create .MAC'
            ],
            default_value='Homepage'),
        sg.Button('Open Chapter', key='-OPEN_URL-')
    ],
    [sg.Exit()],
]  #* Exit Button

window_MAIN = sg.Window(title='DocuPort_PSG',
                        layout=winlayout,
                        element_justification='Center',
                        auto_size_buttons=True,
                        element_padding=(5, 5),
                        margins=((5, 5)))
#^ Displays Window

while True:  #* The Infinite Loop that keeps the Window open, and returns feedback from the user.
    event, values = window_MAIN.read()
    #print(event, values)  #NOTE: #? Enable to print stdout to console.

    #! Closes Window upon clicking 'x' or sg.Exit() Button.
    if (event == sg.WIN_CLOSED or event == 'Exit'):
        break

    if event == '-OPEN_URL-':
        if values['-OPTION_MENU-'] == 'Homepage':
            open_PSGUI(values['-OPTION_MENU-'],
                       'https://pysimplegui.readthedocs.io/en/latest/')

        if values['-OPTION_MENU-'] == 'Learning Resources':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#learning-resources'
            )

        if values['-OPTION_MENU-'] == 'Getting Started':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#getting-started-with-pysimplegui'
            )

        if values['-OPTION_MENU-'] == 'Demo Screenshots':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/screenshots_demos/'
            )

        if values['-OPTION_MENU-'] == 'Call Reference':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/call%20reference/'
            )

        if values['-OPTION_MENU-'] == 'Cookbook':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/cookbook/')

        if values['-OPTION_MENU-'] == 'Readme':
            open_PSGUI(values['-OPTION_MENU-'],
                       'https://pysimplegui.readthedocs.io/en/latest/readme/')

        if values['-OPTION_MENU-'] == 'Popups':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#high-level-api-calls-popups'
            )

        if values['-OPTION_MENU-'] == 'Progress Meters':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#progress-meters'
            )

        if values['-OPTION_MENU-'] == 'Custom Windows':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#custom-window-api-calls-your-first-window'
            )

        if values['-OPTION_MENU-'] == 'Layouts':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#layouts')

        if values['-OPTION_MENU-'] == '-Elements-':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#elements')

        if values['-OPTION_MENU-'] == 'Themes':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#themes-automatic-coloring-of-your-windows'
            )

        if values['-OPTION_MENU-'] == 'Return Values':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#return-values')

        if values['-OPTION_MENU-'] == 'System Tray':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#systemtray')

        if values['-OPTION_MENU-'] == 'Keyboard & Mouse Capture':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#keyboard-mouse-capture'
            )

        if values['-OPTION_MENU-'] == 'Menus':
            open_PSGUI(values['-OPTION_MENU-'],
                       'https://pysimplegui.readthedocs.io/en/latest/#menus')

        if values['-OPTION_MENU-'] == 'Multiple Windows':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#running-multiple-windows'
            )

        if values['-OPTION_MENU-'] == 'Debug':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#the-pysimplegui-debugger'
            )

        if values['-OPTION_MENU-'] == 'User Settings API':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#user-settings-api'
            )

        if values['-OPTION_MENU-'] == 'Extensions':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#extending-pysimplegui'
            )

        if values['-OPTION_MENU-'] == 'Demo Apps':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#demo-programs-applications'
            )

        if values['-OPTION_MENU-'] == 'Create .EXE':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#creating-a-windows-exe-file'
            )

        if values['-OPTION_MENU-'] == 'Create .MAC':
            open_PSGUI(
                values['-OPTION_MENU-'],
                'https://pysimplegui.readthedocs.io/en/latest/#creating-a-mac-app-file'
            )

    window_MAIN['-TEXT_TOP-'].update(
        'Choose a Chapter/Section of the Documentation to Browse')

window_MAIN.close()
