# Primitive script to open Online-Documentation for PySimpleGUI using a console/terminal. #

from typing import Any
from webbrowser import open as openURL
from loadingSequence import load
from sys import exit as ex
from time import sleep as s


def drawMenu() -> None:
    print(""" ___________Menu___________
| 1. Homepage              |
| 2. Getting Started       |
| 3. DemoScreenshots       |
| 4. Call Reference        |
| 5. CookBook              |
| 6. ReadMe                |
| 7. Popups                |
| 8. Progress Meters       |
| 9. My First Window       |
|10. Layouts               |
|11. Elements              |
|12. System Tray Icons     |
|13. Keyboard/Mouse Capture|
|14. Menus                 |
|15. Running Mult. Windows |
|16. Debugging PySimpleGUI |
|17. User Settings API     |
|18. Extending PYSimpleGUI |
|19. Demo Apps             |
|20. Create .EXE File      |
|21. Create MAC File       |
|22. EXIT                  |
|__________________________|""")


def homepage() -> None:
    load('Opening PySimpleGUI Homepage', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/'
    openURL(url, new=2, autoraise=True)


def gettingStarted() -> None:
    load('Opening Docs Chapter: \"Getting Started\"', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#getting-started-with-pysimplegui'
    openURL(url, new=2, autoraise=True)


def demoScreenshots() -> None:
    load('Opening Demo Screenshots', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/screenshots_demos/'
    openURL(url, new=2, autoraise=True)


def callReference() -> None:
    load('Opening Call Reference', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/call%20reference/'
    openURL(url, new=2, autoraise=True)


def cookbook() -> None:
    load('Opening PySimpleGUI Cookbook', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/cookbook/'
    openURL(url, new=2, autoraise=True)


def readme() -> None:
    load('Opening PySimpleGUI Readme', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/readme/'
    openURL(url, new=2, autoraise=True)


def popups() -> None:
    load('Opening \"Popups\" PSG Doc Chapter', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#high-level-api-calls-popups'
    openURL(url, new=2, autoraise=True)


def progressMeters() -> None:
    load('Opening ', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#progress-meters'
    openURL(url, new=2, autoraise=True)


def customWindows() -> None:
    load('Opening \"Custom Windows\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#custom-window-api-calls-your-first-window'
    openURL(url, new=2, autoraise=True)


def layouts() -> None:
    load('Opening \"Layouts\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#layouts'
    openURL(url, new=2, autoraise=True)


def elements() -> None:
    load('Opening \"Elements\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#elements'
    openURL(url, new=2, autoraise=True)


def systemTray() -> None:
    load('Opening \"System Tray\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#systemtray'
    openURL(url, new=2, autoraise=True)


def keyboardMouse_Cap() -> None:
    load('Opening \"Keyboard/Mouse Capture\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#keyboard-mouse-capture'
    openURL(url, new=2, autoraise=True)


def menus() -> None:
    load('Opening \"Menus\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#menud'
    openURL(url, new=2, autoraise=True)


def multipleWindows() -> None:
    load('Opening \"Running Multiple Windows\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#running-multiple-windows'
    openURL(url, new=2, autoraise=True)


def debugger() -> None:
    load('Opening \"The PySimpleGUI Debugger\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#the-pysimplegui-debugger'
    openURL(url, new=2, autoraise=True)


def userSettings_API() -> None:
    load('Opening \"User Settings API\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#user-settings-api'
    openURL(url, new=2, autoraise=True)


def extensions() -> None:
    load('Opening \"Extending PySimpleGUI\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#extending-pysimplegui'
    openURL(url, new=2, autoraise=True)


def demoApps() -> None:
    load('Opening \"\'Demo Programs\' Applications\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#demo-programs-applications'
    openURL(url, new=2, autoraise=True)


def createEXE() -> None:
    load('Opening \"Creating a Windows .EXE File\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#creating-a-windows-exe-file'
    openURL(url, new=2, autoraise=True)


def createMAC() -> None:
    load('Opening \"Creating a MAC App File\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#creating-a-mac-app-file'
    openURL(url, new=2, autoraise=True)


#~ ============================= BEGIN PROGRAM ============================= ~#
inputCount: int = 0
while True:
    if inputCount % 5 == 0:
        drawMenu()
    menuchoice = str(input('\nPlease ENTER an option between [1-22]:\n> '))
    if menuchoice == '1':
        inputCount += 1
        homepage()
    elif menuchoice == '2':
        inputCount += 1
        gettingStarted()
    elif menuchoice == '3':
        inputCount += 1
        demoScreenshots()
    elif menuchoice == '4':
        inputCount += 1
        callReference()
    elif menuchoice == '5':
        inputCount += 1
        cookbook()
    elif menuchoice == '6':
        inputCount += 1
        readme()
    elif menuchoice == '7':
        inputCount += 1
        popups()
    elif menuchoice == '8':
        inputCount += 1
        progressMeters()
    elif menuchoice == '9':
        inputCount += 1
        customWindows()
    elif menuchoice == '10':
        inputCount += 1
        layouts()
    elif menuchoice == '11':
        inputCount += 1
        elements()
    elif menuchoice == '12':
        inputCount += 1
        systemTray()
    elif menuchoice == '13':
        inputCount += 1
        keyboardMouse_Cap()
    elif menuchoice == '14':
        inputCount += 1
        menus()
    elif menuchoice == '15':
        inputCount += 1
        multipleWindows()
    elif menuchoice == '16':
        inputCount += 1
        debugger()
    elif menuchoice == '17':
        inputCount += 1
        userSettings_API()
    elif menuchoice == '18':
        inputCount += 1
        extensions()
    elif menuchoice == '19':
        inputCount += 1
        demoApps()
    elif menuchoice == '20':
        inputCount += 1
        createEXE()
    elif menuchoice == '21':
        inputCount += 1
        createMAC()
    elif menuchoice == '22':
        load('Exiting', 'GoodBye!')
        s(0.2)
        ex(0)
    else:
        inputCount = 0
        print('\n- ERROR: -\n> Must Enter an Integer between 1 and 23.\n')
        s(1)
