### File for using cx_freeze to convert py files into executables

import sys
from cx_Freeze import setup, Executable

build_exe_options =  {"packages": ["os"], "excludes": ["tkinter"]}
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    


setup(
    name = "jbv2022z",
    version = "1.1",
    description = "Test game",
    options = {"build_exe": build_exe_options},
    executables = [Executable("jbv2022z.py", base = base)]
)
