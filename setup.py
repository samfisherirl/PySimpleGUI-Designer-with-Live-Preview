from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [], 'includes': ['tk-tools', 'tkinter', 'ttk', 'ttkwidgets', 'PySimpleGUI']}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(r"C:\Users\dower\OneDrive\__DISCORD_APP\__GPT3____\SimpleGUIBuilder-main\SimpleGUIBuilder\live_preview.py", base=base, icon = "C:\\Users\\dower\\Documents\\virtual-reality.ico")]

setup(name='live_preview',
      version = '1.0',
      description = '',
      options = {'build_exe': {"include_files": ["autosave.txt", "default.txt", "theme.txt"] } },
      executables = executables)
