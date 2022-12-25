"""
Use pywinauto with notepad
"""

from turtle import title
from pywinauto import Application

# start, connect app
# app = Application(backend="uia").start(r'C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2208.25.0_x64__8wekyb3d8bbwe\Notepad\notepad.exe').connect(title="Untitled - Notepad")
app = Application(backend="uia").start(r'notepad.exe').connect(title='Untitled - Notepad')

notepad_window = app.window(title_re='.* - Notepad')

# Print all elements of the window
# notepad_window.print_control_identifiers

