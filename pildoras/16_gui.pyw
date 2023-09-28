"""
Class 42: Graphic interfaces part 1: Intro to tkinter
Author: Eliana Chavez
"""
# Other libraries to build gui: WxPython PyQT PyGTK
from tkinter import *  # TCL/TK

# Root (tk) -> Frame -> Widgets

root = Tk()
root.title("Custom title")
root.resizable(False, False)
root.geometry("650x350")
root.config(bg="pink")
# Change default icon, should have a .ico image in the same folder
try:
    root.iconbitmap("icon.ico")
except:
    print("Icon not set")

root.mainloop()
