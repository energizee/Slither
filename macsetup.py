application_title = "Slither" 
main_python_file = "Slither.py" 

import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re"]

setup(
        name = application_title,
        version = "1.1",
        description = "Slither, a remake of the classic snake game.",
        options = {"build_exe" :{"packages":["pygame"], {"includes" :["snakehead.png", "apple.png"]}},
        executables = [Executable(main_python_file, base = base)])
        
