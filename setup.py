### File for using cx_freeze to convert py files into executables
### To create a new exe file, enter into dos prompt and type:
### python setup.py build
### Then copy the new files in the subdirectory into the main game directory

import sys
from cx_Freeze import setup, Executable

build_exe_options =  {"packages": ["os"], "excludes": ["tkinter"]}
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    


setup(
    name = "Minoan RPG",
    version = "0.2",
    description = "JCB 2022 game",
    options = {"build_exe": build_exe_options},
    executables = [Executable("MinoanRPGEXE4.py", base = base)]
)
