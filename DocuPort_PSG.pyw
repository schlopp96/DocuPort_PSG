#
# Simple GUI Script to open Online-Documentation for PySimpleGUI and redirects the user to the specific documentation chapter desired.

from random import choice as rChoice
from sys import exit as ex
from time import sleep as s
from webbrowser import open

import PySimpleGUI as sg
from loadingSequence import load


def homepage():
    """Opens PySimpleGUI Documentation Homepage in the user's default browser."""
    load("Opening PySimpleGUI Homepage", "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/"
    open(url, new=2, autoraise=True)


def learningResources():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Learning Resources"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#learning-resources"
    open(url, new=2, autoraise=True)


def gettingStarted():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Getting Started"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#getting-started-with-pysimplegui"
    open(url, new=2, autoraise=True)


def demoScreenshots():
    """Opens PySimpleGUI "Screenshots Demos" Webpage in the User's Default Browser."""
    load('Opening Doc Section: "Demo Screenshots"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/screenshots_demos/"
    open(url, new=2, autoraise=True)


def callReference():
    """Opens PySimpleGUI "Call Reference" Webpage in the User's Default Browser."""
    load('Opening PySimpleGUI "Call Reference" Page', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/call%20reference/"
    open(url, new=2, autoraise=True)


def cookbook():
    """Opens PySimpleGUI Cookbook in the User's Default Browser."""
    load('Opening PySimpleGUI "Cookbook" Page', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/cookbook/"
    open(url, new=2, autoraise=True)


def readme():
    """Opens Specific PySimpleGUI Documentation README in the User's Default Browser."""
    load('Opening PySimpleGUI "Readme" Page', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/readme/"
    open(url, new=2, autoraise=True)


def popups():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Popups" PSG Doc Chapter', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#high-level-api-calls-popups"
    open(url, new=2, autoraise=True)


def progressMeters():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Progress Meters"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#progress-meters"
    open(url, new=2, autoraise=True)


def customWindows():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Custom Windows"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#custom-window-api-calls-your-first-window"
    open(url, new=2, autoraise=True)


def layouts():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Layouts"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#layouts"
    open(url, new=2, autoraise=True)


def elements():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Elements"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#elements"
    open(url, new=2, autoraise=True)


def returnValues():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Return Values"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#return-values"
    open(url, new=2, autoraise=True)


def themes():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Themes - Automatic Colouring of Your Windows"',
         "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#themes-automatic-coloring-of-your-windows"
    open(url, new=2, autoraise=True)


def systemTray():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "System Tray"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#systemtray"
    open(url, new=2, autoraise=True)


def keyboardMouse_Cap():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Keyboard/Mouse Capture"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#keyboard-mouse-capture"
    open(url, new=2, autoraise=True)


def menus():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Menus"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#menus"
    open(url, new=2, autoraise=True)


def multipleWindows():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Running Multiple Windows"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#running-multiple-windows"
    open(url, new=2, autoraise=True)


def debugger():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "The PySimpleGUI Debugger"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#the-pysimplegui-debugger"
    open(url, new=2, autoraise=True)


def userSettings_API():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "User Settings API"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#user-settings-api"
    open(url, new=2, autoraise=True)


def extensions():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Extending PySimpleGUI"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#extending-pysimplegui"
    open(url, new=2, autoraise=True)


def demoPrograms():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Demo Programs\\Applications"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#demo-programs-applications"
    open(url, new=2, autoraise=True)


def createEXE():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Creating a Windows .EXE File"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#creating-a-windows-exe-file"
    open(url, new=2, autoraise=True)


def createMAC():
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    load('Opening Doc Section: "Creating a MAC App File"', "Done!")
    url = r"https://pysimplegui.readthedocs.io/en/latest/#creating-a-mac-app-file"
    open(url, new=2, autoraise=True)


def randomTheme():  # Randomizes Color Theme on Launch
    """Opens Specific PySimpleGUI Documentation Chapter in the User's Default Browser."""
    themeChoices = [
        "Black",
        "BlueMono",
        "BluePurple",
        "BrightColors",
        "BrownBlue",
        "Dark",
        "Dark2",
        "DarkAmber",
        "DarkBlack",
        "DarkBlack1",
        "DarkBlue",
        "DarkBlue1",
        "DarkBlue10",
        "DarkBlue11",
        "DarkBlue12",
        "DarkBlue13",
        "DarkBlue14",
        "DarkBlue15",
        "DarkBlue16",
        "DarkBlue17",
        "DarkBlue2",
        "DarkBlue3",
        "DarkBlue4",
        "DarkBlue5",
        "DarkBlue6",
        "DarkBlue7",
        "DarkBlue8",
        "DarkBlue9",
        "DarkBrown",
        "DarkBrown1",
        "DarkBrown2",
        "DarkBrown3",
        "DarkBrown4",
        "DarkBrown5",
        "DarkBrown6",
        "DarkBrown7",
        "DarkGreen",
        "DarkGreen1",
        "DarkGreen2",
        "DarkGreen3",
        "DarkGreen4",
        "DarkGreen5",
        "DarkGreen6",
        "DarkGreen7",
        "DarkGrey",
        "DarkGrey1",
        "DarkGrey10",
        "DarkGrey11",
        "DarkGrey12",
        "DarkGrey13",
        "DarkGrey14",
        "DarkGrey2",
        "DarkGrey3",
        "DarkGrey4",
        "DarkGrey5",
        "DarkGrey6",
        "DarkGrey7",
        "DarkGrey8",
        "DarkGrey9",
        "DarkPurple",
        "DarkPurple1",
        "DarkPurple2",
        "DarkPurple3",
        "DarkPurple4",
        "DarkPurple5",
        "DarkPurple6",
        "DarkPurple7",
        "DarkRed",
        "DarkRed1",
        "DarkRed2",
        "DarkTanBlue",
        "DarkTeal",
        "DarkTeal1",
        "DarkTeal10",
        "DarkTeal11",
        "DarkTeal12",
        "DarkTeal2",
        "DarkTeal3",
        "DarkTeal4",
        "DarkTeal5",
        "DarkTeal6",
        "DarkTeal7",
        "DarkTeal8",
        "DarkTeal9",
        "Default",
        "Default1",
        "DefaultNoMoreNagging",
        "Green",
        "GreenMono",
        "GreenTan",
        "HotDogStand",
        "Kayak",
        "LightBlue",
        "LightBlue1",
        "LightBlue2",
        "LightBlue3",
        "LightBlue4",
        "LightBlue5",
        "LightBlue6",
        "LightBlue7",
        "LightBrown",
        "LightBrown1",
        "LightBrown10",
        "LightBrown11",
        "LightBrown12",
        "LightBrown13",
        "LightBrown2",
        "LightBrown3",
        "LightBrown4",
        "LightBrown5",
        "LightBrown6",
        "LightBrown7",
        "LightBrown8",
        "LightBrown9",
        "LightGray1",
        "LightGreen",
        "LightGreen1",
        "LightGreen10",
        "LightGreen2",
        "LightGreen3",
        "LightGreen4",
        "LightGreen5",
        "LightGreen6",
        "LightGreen7",
        "LightGreen8",
        "LightGreen9",
        "LightGrey",
        "LightGrey1",
        "LightGrey2",
        "LightGrey3",
        "LightGrey4",
        "LightGrey5",
        "LightGrey6",
        "LightPurple",
        "LightTeal",
        "LightYellow",
        "Material1",
        "Material2",
        "NeutralBlue",
        "Purple",
        "Python",
        "Reddit",
        "Reds",
        "SandyBeach",
        "SystemDefault",
        "SystemDefault1",
        "SystemDefaultForReal",
        "Tan",
        "TanBlue",
        "TealMono",
        "Topanga",
    ]
    return rChoice((themeChoices))


sg.theme(randomTheme()
         )  # Changes the base color layout each time the app is opened.

winlayout = [
    [sg.Text("Choose a Chapter/Section of the Documentation to Browse")
     ],  # Title Of Window
    [sg.Button("Homepage", key="-Homepage-")],  # Button Row 1
    [
        sg.Button("Learning Resources", key="-Learning Resources-"),
        sg.Button("Getting Started", key="-Getting Started-"),
        sg.Button("Cookbook", key="-Cookbook-"),
    ],  # Button Row 2
    [sg.Button("Demo Screenshots", key="-Demo Screenshots-")],
    [
        sg.Button("Call Reference", key="-Call Reference-"),
        sg.Button("Readme", key="-Readme-"),
    ],  # Button Row 3
    [
        sg.Button("Popups", key="-Popups-"),
        sg.Button("Progress Meters", key="-Progress Meters-"),
        sg.Button("Custom Windows", key="-Custom Windows-"),
    ],  # Button Row 4
    [
        sg.Button("Layouts", key="-Layouts-"),
        sg.Button("Elements", key="-Elements-"),
        sg.Button("Themes", key="-Themes-"),
        sg.Button("Return Values", key="-Return Values-"),
    ],  # Button Row 5
    [
        sg.Button("Keyboard & Mouse Capture",
                  key="-Keyboard & Mouse Capture-"),
        sg.Button("Menus", key="-Menus-"),
        sg.Button("System Tray", key="-System Tray-"),
    ],  # Button Row 6
    [
        sg.Button("Multiple Windows", key="-Multiple Windows-"),
        sg.Button("Debugger", key="-Debugger-"),
        sg.Button("User Settings API", key="-User Settings API-"),
        sg.Button("Extensions", key="-Extensions-"),
    ],  # Button Row 7
    [
        sg.Button("Demo Apps", key="-Demo Apps-"),
        sg.Button("Create .EXE", key="-Create .EXE-"),
        sg.Button("Create .MAC", key="-Create .MAC-"),
    ],  # Button Row 8
    [sg.Exit()],
]  # Button Row 9

window = sg.Window(title="DocuPort_PSG",
                   layout=winlayout,
                   element_justification="Center",
                   default_button_element_size=(20, 1),
                   element_padding=(5, 5),
                   margins=((5,5)))
# Displays Window

while True:  # The Infinite Loop that keeps the Window open, and returns feedback from the user.
    event, values = window.read()
    print(event, values)
    if (event == sg.WIN_CLOSED or event == "Exit"
        ):  # Closes upon clicking the "x" or clicking the sg.Exit() Button.
        break
    if event == "-Homepage-":
        homepage()
    if event == "-Learning Resources-":
        learningResources()
    if event == "-Getting Started-":
        gettingStarted()
    if event == "-Demo Screenshots-":
        demoScreenshots()
    if event == "-Call Reference-":
        callReference()
    if event == "-Cookbook-":
        cookbook()
    if event == "-Readme-":
        readme()
    if event == "-Popups-":
        popups()
    if event == "-Progress Meters-":
        progressMeters()
    if event == "-Custom Windows-":
        customWindows()
    if event == "-Layouts-":
        layouts()
    if event == "-Elements-":
        elements()
    if event == "-Themes-":
        themes()
    if event == "-Return Values-":
        returnValues()
    if event == "-System Tray-":
        systemTray()
    if event == "-Keyboard & Mouse Capture-":
        keyboardMouse_Cap()
    if event == "-Menus-":
        menus()
    if event == "-Multiple Windows-":
        multipleWindows()
    if event == "-Debug-":
        debugger()
    if event == "-User Settings API-":
        userSettings_API()
    if event == "-Extensions-":
        extensions()
    if event == "-Demo Apps-":
        demoPrograms()
    if event == "-Create .EXE-":
        createEXE()
    if event == "-Create .MAC-":
        createMAC()

window.close()
