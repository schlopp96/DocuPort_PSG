# Primitive script to open Online-Documentation for PySimpleGUI using a console/terminal. #

from typing import Any
from webbrowser import open as openURL
from loadingSequence import load
from sys import exit as ex
from time import sleep as s


def drawMenu() -> None:
    print('''\t      ___________Menu___________
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
             |__________________________|''')


def homepage() -> Any:
    load('Opening PySimpleGUI Homepage', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/'
    return openURL(url, new=2, autoraise=True)


def gettingStarted() -> Any:
    load('Opening Docs Chapter: \"Getting Started\"', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#getting-started-with-pysimplegui'
    return openURL(url, new=2, autoraise=True)


def demoScreenshots() -> Any:
    load('Opening Demo Screenshots', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/screenshots_demos/'
    return openURL(url, new=2, autoraise=True)


def callReference() -> Any:
    load('Opening Call Reference', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/call%20reference/'
    return openURL(url, new=2, autoraise=True)


def cookbook() -> Any:
    load('Opening PySimpleGUI Cookbook', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/cookbook/'
    return openURL(url, new=2, autoraise=True)


def readme() -> Any:
    load('Opening PySimpleGUI Readme', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/readme/'
    return openURL(url, new=2, autoraise=True)


def popups() -> Any:
    load('Opening \"Popups\" PSG Doc Chapter', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#high-level-api-calls-popups'
    return openURL(url, new=2, autoraise=True)


def progressMeters() -> Any:
    load('Opening ', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#progress-meters'
    return openURL(url, new=2, autoraise=True)


def customWindows() -> Any:
    load('Opening \"Custom Windows\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#custom-window-api-calls-your-first-window'
    return openURL(url, new=2, autoraise=True)


def layouts() -> Any:
    load('Opening \"Layouts\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#layouts'
    return openURL(url, new=2, autoraise=True)


def elements() -> Any:
    load('Opening \"Elements\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#elements'
    return openURL(url, new=2, autoraise=True)


def systemTray() -> Any:
    load('Opening \"System Tray\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#systemtray'
    return openURL(url, new=2, autoraise=True)


def keyboardMouse_Cap() -> Any:
    load('Opening \"Keyboard/Mouse Capture\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#keyboard-mouse-capture'
    return openURL(url, new=2, autoraise=True)


def menus() -> Any:
    load('Opening \"Menus\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#menud'
    return openURL(url, new=2, autoraise=True)


def multipleWindows() -> Any:
    load('Opening \"Running Multiple Windows\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#running-multiple-windows'
    return openURL(url, new=2, autoraise=True)


def debugger() -> Any:
    load('Opening \"The PySimpleGUI Debugger\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#the-pysimplegui-debugger'
    return openURL(url, new=2, autoraise=True)


def userSettings_API() -> Any:
    load('Opening \"User Settings API\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#user-settings-api'


def extensions() -> Any:
    load('Opening \"Extending PySimpleGUI\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#extending-pysimplegui'
    return openURL(url, new=2, autoraise=True)


def demoApps() -> Any:
    load('Opening \"\'Demo Programs\' Applications\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#demo-programs-applications'
    return openURL(url, new=2, autoraise=True)


def createEXE() -> Any:
    load('Opening \"Creating a Windows .EXE File\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#creating-a-windows-exe-file'
    return openURL(url, new=2, autoraise=True)


def createMAC() -> Any:
    load('Opening \"Creating a MAC App File\" Doc Section', 'Done!')
    url = r'https://pysimplegui.readthedocs.io/en/latest/#creating-a-mac-app-file'
    return openURL(url, new=2, autoraise=True)




#~ ============================= BEGIN PROGRAM ============================= ~#
inputCount: int = 0
while True:
    if inputCount % 5 == 0:
        drawMenu()
    menuchoice = str(input('Please ENTER an option between [1-22]:\n> '))
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
        print('\n= ERROR =:\n> Must Enter an Integer between 1 and 22.\n')
        s(1)
